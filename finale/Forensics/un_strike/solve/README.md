Il existe d'inombrable script permettant d'analyser des beacons CobaltStrike mais on va utiliser celui du boss [DidierStevens](https://github.com/DidierStevens/DidierStevensSuite/blob/master/1768.py)

```
$ python3 /mnt/d/Download/workshop-cs/DidierStevensSuite/DidierStevensSuite/1768.py malicious.dmp
File: malicious.dmp
xorkey b'.' 2e
0x0001 payload type                     0x0001 0x0002 0 windows-beacon_http-reverse_http
0x0002 port                             0x0001 0x0002 80
0x0003 sleeptime                        0x0002 0x0004 60000
0x0004 maxgetsize                       0x0002 0x0004 1048576
0x0005 jitter                           0x0001 0x0002 0
0x0007 publickey                        0x0003 0x0100 30819f300d06092a864886f70d010101050003818d003081890281810093fad989ca301e1c35ea388ed3e0f8d103d7a021ee7dfc75d7084c7bcdf6a799fb4f0f8f008202f7b2c529632bf63572d2dc5029b7857790c5d2006d480100679c29bbfef2a021ad88fb6a0e26d3cd5bd7f6ddd620390cd4748f95ca11b86b641973a1a9b6cde3fa10987911a9ff4a57e4af084f810d40cef98ceb8956e6eb23020301000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 Has known private key
0x0008 server,get-uri                   0x0003 0x0100 '10.10.10.10,/push'
0x0043 DNS_STRATEGY                     0x0001 0x0002 0
0x0044 DNS_STRATEGY_ROTATE_SECONDS      0x0002 0x0004 -1
0x0045 DNS_STRATEGY_FAIL_X              0x0002 0x0004 -1
0x0046 DNS_STRATEGY_FAIL_SECONDS        0x0002 0x0004 -1
0x000e SpawnTo                          0x0003 0x0010 (NULL ...)
0x001d spawnto_x86                      0x0003 0x0040 '%windir%\\syswow64\\rundll32.exe'
0x001e spawnto_x64                      0x0003 0x0040 '%windir%\\sysnative\\rundll32.exe'
0x001f CryptoScheme                     0x0001 0x0002 0
0x001a get-verb                         0x0003 0x0010 'GET'
0x001b post-verb                        0x0003 0x0010 'POST'
0x001c HttpPostChunk                    0x0002 0x0004 0
0x0025 license-id                       0x0002 0x0004 0 trial or pirated? - Stats uniques -> ips/hostnames: 750 publickeys: 452
0x0026 bStageCleanup                    0x0001 0x0002 0
0x0027 bCFGCaution                      0x0001 0x0002 0
0x0009 useragent                        0x0003 0x0100 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)'
0x000a post-uri                         0x0003 0x0040 '/submit.php'
0x000b Malleable_C2_Instructions        0x0003 0x0100
  Transform Input: [7:Input,4]
   Print
0x000c http_get_header                  0x0003 0x0200
  Build Metadata: [7:Metadata,3,6:Cookie]
   BASE64
   Header Cookie
0x000d http_post_header                 0x0003 0x0200
  Const_header Content-Type: application/octet-stream
  Build SessionId: [7:SessionId,5:id]
   Parameter id
  Build Output: [7:Output,4]
   Print
0x0036 HostHeader                       0x0003 0x0080 (NULL ...)
0x0032 UsesCookies                      0x0001 0x0002 1
0x0023 proxy_type                       0x0001 0x0002 2 IE settings
0x003a TCP_FRAME_HEADER                 0x0003 0x0080 '\x00\x04'
0x0039 SMB_FRAME_HEADER                 0x0003 0x0080 '\x00\x04'
0x0037 EXIT_FUNK                        0x0001 0x0002 0
0x0028 killdate                         0x0002 0x0004 0
0x0029 textSectionEnd                   0x0002 0x0004 0
0x002b process-inject-start-rwx         0x0001 0x0002 64 PAGE_EXECUTE_READWRITE
0x002c process-inject-use-rwx           0x0001 0x0002 64 PAGE_EXECUTE_READWRITE
0x002d process-inject-min_alloc         0x0002 0x0004 0
0x002e process-inject-transform-x86     0x0003 0x0100 (NULL ...)
0x002f process-inject-transform-x64     0x0003 0x0100 (NULL ...)
0x0035 process-inject-stub              0x0003 0x0010 'ä:\x05QS\x927\x8aìr\x94Kâ\x18\x0fz'
0x0033 process-inject-execute           0x0003 0x0080 '\x01\x02\x03\x04'
0x0034 process-inject-allocation-method 0x0001 0x0002 0
0x0000
Guessing Cobalt Strike version: 4.3 (max 0x0046)
Sanity check Cobalt Strike config: OK
Runtime config 32-bit found: 0x00510e80
0x0001 payload type                     0x0001 0x0002 0 windows-beacon_http-reverse_http
0x0002 port                             0x0001 0x0002 80
0x0003 sleeptime                        0x0002 0x0004 60000
0x0004 maxgetsize                       0x0002 0x0004 1048576
0x0005 jitter                           0x0001 0x0002 0
0x0007 publickey                        0x0003 0x0100 30819f300d06092a864886f70d010101050003818d003081890281810093fad989ca301e1c35ea388ed3e0f8d103d7a021ee7dfc75d7084c7bcdf6a799fb4f0f8f008202f7b2c529632bf63572d2dc5029b7857790c5d2006d480100679c29bbfef2a021ad88fb6a0e26d3cd5bd7f6ddd620390cd4748f95ca11b86b641973a1a9b6cde3fa10987911a9ff4a57e4af084f810d40cef98ceb8956e6eb23020301000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 Has known private key
0x0008 server,get-uri                   0x0003 0x0100 '10.10.10.10,/push'
0x0009 useragent                        0x0003 0x0100 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)'
0x000a post-uri                         0x0003 0x0100 '/submit.php'
0x000b Malleable_C2_Instructions        0x0003 0x0100
  Transform Input: [7:Input,4]
   Print
0x000c http_get_header                  0x0003 0x0100
  Build Metadata: [7:Metadata,3,6:Cookie]
   BASE64
   Header Cookie
0x000d http_post_header                 0x0003 0x0100
  Const_header Content-Type: application/octet-stream
  Build SessionId: [7:SessionId,5:id]
   Parameter id
  Build Output: [7:Output,4]
   Print
0x000e SpawnTo                          0x0003 0x0100 (NULL ...)
0x001a get-verb                         0x0003 0x0100 'GET'
0x001b post-verb                        0x0003 0x0100 'POST'
0x001c HttpPostChunk                    0x0002 0x0004 0
0x001d spawnto_x86                      0x0003 0x0100 '%windir%\\syswow64\\rundll32.exe'
0x001e spawnto_x64                      0x0003 0x0100 '%windir%\\sysnative\\rundll32.exe'
0x001f CryptoScheme                     0x0001 0x0002 0
0x0023 proxy_type                       0x0001 0x0002 2 IE settings
0x0025 license-id                       0x0002 0x0004 0 trial or pirated? - Stats uniques -> ips/hostnames: 750 publickeys: 452
0x0026 bStageCleanup                    0x0001 0x0002 0
0x0027 bCFGCaution                      0x0001 0x0002 0
0x0028 killdate                         0x0002 0x0004 0
0x0029 textSectionEnd                   0x0002 0x0004 0
0x002b process-inject-start-rwx         0x0001 0x0002 64 PAGE_EXECUTE_READWRITE
0x002c process-inject-use-rwx           0x0001 0x0002 64 PAGE_EXECUTE_READWRITE
0x002d process-inject-min_alloc         0x0002 0x0004 0
0x002e process-inject-transform-x86     0x0003 0x0100 (NULL ...)
0x002f process-inject-transform-x64     0x0003 0x0100 (NULL ...)
0x0032 UsesCookies                      0x0001 0x0002 1
0x0033 process-inject-execute           0x0003 0x0100 '\x01\x02\x03\x04'
0x0034 process-inject-allocation-method 0x0001 0x0002 0
0x0035 process-inject-stub              0x0003 0x0100 'ä:\x05QS\x927\x8aìr\x94Kâ\x18\x0fz¯\x86ø0£\x86'
0x0036 HostHeader                       0x0003 0x0100 (NULL ...)
0x0037 EXIT_FUNK                        0x0001 0x0002 0
0x0039 SMB_FRAME_HEADER                 0x0003 0x0100 (NULL ...)
0x003a TCP_FRAME_HEADER                 0x0003 0x0100 (NULL ...)
0x0043 DNS_STRATEGY                     0x0001 0x0002 0
0x0044 DNS_STRATEGY_ROTATE_SECONDS      0x0002 0x0004 -1
0x0045 DNS_STRATEGY_FAIL_X              0x0002 0x0004 -1
0x0046 DNS_STRATEGY_FAIL_SECONDS        0x0002 0x0004 -1
0x0000
Guessing Cobalt Strike version: 4.3 (max 0x0046)
Sanity check Cobalt Strike config: OK
Sleep mask 32-bit 4.2 deobfuscation routine found: 0x0009e345 (LSFIF: b'Y_^[')
Sleep mask 32-bit 4.2 deobfuscation routine found: 0x000d2f45 (LSFIF: b'Y_^[')
Public key config entry found: 0x000caead (xorKey b'.') (LSFIF: b'././.,...,./.,.~.-.,.*..')
Public key header found: 0x0016fae1 (LSFIF: b'!')
```

On a donc :
- payload type 0x0001 0x0002 0 windows-beacon_http-reverse_http
- server,get-uri 0x0003 0x0100 '10.10.10.10,/push'
- post-uri 0x0003 0x0100 '/submit.php'