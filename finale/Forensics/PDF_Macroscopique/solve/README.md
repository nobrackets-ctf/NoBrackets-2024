```
$ python3 /home/shaym/DidierStevensSuite/pdf-parser.py -a 05d8bc12d167cf6d1f56bfa8060b10f92c5688f960a2a34e2983be4739e60808.pdf.vir
This program has not been tested with this version of Python (3.11.9)
Should you encounter problems, please use Python version 3.11.1
Comment: 3
XREF: 0
Trailer: 0
StartXref: 1
Indirect object: 10
Indirect objects with a stream: 12, 13, 14, 21, 22, 24, 1, 26
  4: 12, 13, 14, 25
 /Catalog 1: 2
 /EmbeddedFile 1: 22
 /ObjStm 1: 1
 /XObject 2: 21, 24
 /XRef 1: 26
Unreferenced indirect objects: 1 0 R, 12 0 R, 13 0 R, 14 0 R, 21 0 R, 22 0 R, 26 0 R
Unreferenced indirect objects without /ObjStm objects: 12 0 R, 13 0 R, 14 0 R, 21 0 R, 22 0 R, 26 0 R
Search keywords:
 /OpenAction 1: 2
 /AcroForm 1: 2
 /EmbeddedFile 1: 22
```

```
$ python3 /home/shaym/DidierStevensSuite/pdf-parser.py -f 05d8bc12d167cf6d1f56bfa8060b10f92c5688f960a2a34e2983be4739e60808.pdf.vir --search openaction
This program has not been tested with this version of Python (3.11.9)
Should you encounter problems, please use Python version 3.11.1
obj 2 0
 Type: /Catalog
 Referencing: 4 0 R, 5 0 R, 6 0 R, 7 0 R, 8 0 R

  <<
    /Type /Catalog
    /Outlines 4 0 R
    /Pages 5 0 R
    /Names 6 0 R
    /OpenAction 7 0 R
    /AcroForm 8 0 R
  >>

 [(1, '\n'), (2, '<<'), (1, '\n'), (2, '/Type'), (1, ' '), (2, '/Catalog'), (1, '\n'), (2, '/Outlines'), (1, ' '), (3, '4'), (1, ' '), (3, '0'), (1, ' '), (3, 'R'), (1, '\n'), (2, '/Pages'), (1, ' '), (3, '5'), (1, ' '), (3, '0'), (1, ' '), (3, 'R'), (1, '\n'), (2, '/Names'), (1, ' '), (3, '6'), (1, ' '), (3, '0'), (1, ' '), (3, 'R'), (1, '\n'), (2, '/OpenAction'), (1, ' '), (3, '7'), (1, ' '), (3, '0'), (1, ' '), (3, 'R'), (1, '\n'), (2, '/AcroForm'), (1, ' '), (3, '8'), (1, ' '), (3, '0'), (1, ' '), (3, 'R'), (1, '\n'), (2, '>>'), (1, '\n')]
```
```
$ python3 /home/shaym/DidierStevensSuite/pdf-parser.py -f sample1 -o 22 -raw
This program has not been tested with this version of Python (3.11.8)
Should you encounter problems, please use Python version 3.11.1
obj 22 0
 Type: /EmbeddedFile
 Referencing:
 Contains stream

  <<
    /Filter /FlateDecode
    /Type /EmbeddedFile
    /Length 45835
  >>

b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1\x00\x00\x00\x00\x00[...]\x84\xe3^E\x16\xbb-V>\xc9\xd6A\xb2,F#\xd4\xb3\xed'
```
```
$ python3 /home/shaym/DidierStevensSuite/pdf-parser.py --object 22 -f -w -d macro1 05d8bc12d167cf6d1f56bfa8060b10f92c5
688f960a2a34e2983be4739e60808.pdf.vir
This program has not been tested with this version of Python (3.11.9)
Should you encounter problems, please use Python version 3.11.1
obj 22 0
 Type: /EmbeddedFile
 Referencing:
 Contains stream

  <<
    /Filter /FlateDecode
    /Type /EmbeddedFile
    /Length 45835
  >>

$ file macro1
macro1: CDFV2 Encrypted
-> Office File Encrypted with password
```
```
$ oleid macro1
XLMMacroDeobfuscator: pywin32 is not installed (only is required if you want to use MS Excel)
oleid 0.60.1 - http://decalage.info/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues

Filename: macro1
--------------------+--------------------+----------+--------------------------
Indicator           |Value               |Risk      |Description
--------------------+--------------------+----------+--------------------------
File format         |Generic OLE file /  |info      |Unrecognized OLE file.
                    |Compound File       |          |Root CLSID:  - None
                    |(unknown format)    |          |
--------------------+--------------------+----------+--------------------------
Container format    |OLE                 |info      |Container type
--------------------+--------------------+----------+--------------------------
Encrypted           |True                |low       |The file is encrypted. It
                    |                    |          |may be decrypted with
                    |                    |          |msoffcrypto-tool
--------------------+--------------------+----------+--------------------------
VBA Macros          |No                  |none      |This file does not contain
                    |                    |          |VBA macros.
--------------------+--------------------+----------+--------------------------
XLM Macros          |No                  |none      |This file does not contain
                    |                    |          |Excel 4/XLM macros.
--------------------+--------------------+----------+--------------------------
External            |0                   |none      |External relationships
Relationships       |                    |          |such as remote templates,
                    |                    |          |remote OLE objects, etc
--------------------+--------------------+----------+--------------------------
```
```
$ python3 /home/shaym/DidierStevensSuite/msoffcrypto-crack.py macro1
Password found: VelvetSweatshop
$ msoffcrypto-tool macro1 macro1_dec -p VelvetSweatshop
```
[msoffcrypto-tool](https://pypi.org/project/msoffcrypto-tool/)
```
$ unzip macro1_dec
Archive:  macro1_dec
  inflating: [Content_Types].xml
  inflating: _rels/.rels
  inflating: xl/_rels/workbook.xml.rels
  inflating: xl/workbook.xml
  inflating: xl/theme/theme1.xml
  inflating: xl/worksheets/sheet2.xml
  inflating: xl/worksheets/_rels/sheet1.xml.rels
  inflating: xl/worksheets/_rels/sheet2.xml.rels
  inflating: xl/drawings/_rels/drawing1.xml.rels
  inflating: xl/worksheets/sheet3.xml
 extracting: xl/media/image1.png
  inflating: xl/drawings/drawing1.xml
  inflating: xl/embeddings/oleObject1.bin
  inflating: xl/drawings/vmlDrawing1.vml
  inflating: xl/styles.xml
  inflating: xl/worksheets/sheet1.xml
  inflating: docProps/core.xml
  inflating: docProps/app.xml
```
```
$ cat extract/xl/embeddings/oleObject1.bin
��ࡱ␦�>��        ������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������Root Entry���������F�I��R!��Ole
�����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������7&�v�)����y������K�
                                                                  �https://2url.one/nVCP6��Q��U�����V���ۥ�␦���[��q��\vq\_ɫ�
����s����4��L����q�xˎ2���v�t�����o��'
                                     ���'���ѧ���E������nhRUUKgIJTNiIvf2GlUqr1XeeGUfVWuJqkuDzzHxxioWvH5wzsXfkcdRH8V8nbiMt���I,�8^d;���␦]�{
```
[Analyse Tria.ge](https://tria.ge/220216-v88kysdcck/behavioral2)

[VT URL](https://www.virustotal.com/gui/url/ead8f2d2e6669952ab8f03b8703579d37c3e045db96d72e57cffa68dc08e6e95)

[VT Stage 2](https://www.virustotal.com/gui/file/c9e2821f3e10c7c2a012d0926f25826c402bd5a6a1e6a1879212b9241cfad8ea/behavior)

```
c9e2821f3e10c7c2a012d0926f25826c402bd5a6a1e6a1879212b9241cfad8ea
```