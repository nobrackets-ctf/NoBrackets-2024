from flask import Flask
from collections import deque
from random import randbytes, randrange, choice
from base64 import urlsafe_b64encode

app = Flask(__name__)

pas=deque(maxlen=1000)
sessions={}

NUM_TREES=3000
cuttedTrees=0
trees=[[randrange(30,400)*choice([1,-1]),randrange(30,400)*choice([1,-1]),0] for _ in range(NUM_TREES)]
reverse_search={f"{tree[0]}{tree[1]}":idx for idx,tree in enumerate(trees)}


@app.route("/trees")
def sendTrees():
    return ';'.join(f"{tree[0]},{tree[1]},{tree[2]}" for tree in trees)

@app.route("/step/<x>+<y>")
def snowSteps(x, y):
    x = int(float(x))
    y = int(float(y))
    pas.append((x,y))
    return "😁👍"

@app.route("/steps")
def showSteps():
    return ";".join(f"{p[0]},{p[1]}" for p in pas)
    """res=b''
    for p in pas:
        res+=p[0].to_bytes(4,byteorder='big').zfill(4)
        res+=p[1].to_bytes(4,byteorder='big').zfill(4)
    return res"""

@app.route("/cut/<x>+<y>+<session_id>")
def cuttingTree(x, y, session_id):
    global trees
    global reverse_search
    global cuttedTrees
    if session_id in sessions and sessions[session_id][0]<1000:
        sessions[session_id][0]+=1
        if x+y in reverse_search: # check arbre existe
            idx = reverse_search.pop(x+y)
            trees[idx][2]=1
            cuttedTrees+=1
            sessions[session_id][1]+=1
            if cuttedTrees>NUM_TREES*0.9:
                trees=[[randrange(30,400)*choice([1,-1]),randrange(30,400)*choice([1,-1]),0] for _ in range(NUM_TREES)]
                reverse_search={f"{tree[0]}{tree[1]}":idx for idx,tree in enumerate(trees)}
                cuttedTrees=0
            return "😁👍"
    return '💀'

@app.route("/session")
def newSession():
    rand_id = urlsafe_b64encode(randbytes(32)).decode('utf-8')
    sessions[rand_id] = [0,0] # Limite (anti Bruteforce),Score
    return rand_id

@app.route("/flag/<session_id>")
def giveFlag(session_id):
    if session_id in sessions and sessions[session_id][1]>500:
        return "NBCTF{Allez_on_y_retourne!Chop_chop!}"
    else:
        return "💀 you thought ?"

app.run(host="0.0.0.0", port=5000, threaded=True)
