from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import sys
root=Path(__file__).resolve().parents[1]/'site';errors=[];pages=list(root.rglob('*.html'));count=0
class Check(HTMLParser):
 def __init__(self,path):super().__init__();self.path=path;self.h1=0;self.titles=0
 def handle_starttag(self,tag,attrs):
  global count
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='title':self.titles+=1
  if tag=='img' and not a.get('alt'):errors.append(f'{self.path}: missing image alt')
  for key in ['href','src']:
   v=a.get(key,'')
   if not v.startswith('/') or v.startswith('//'):continue
   count+=1;p=root/urlsplit(v).path.lstrip('/')
   if not p.exists():errors.append(f'{self.path}: missing {v}')
for p in pages:
 c=Check(p);c.feed(p.read_text());
 if c.h1!=1 or c.titles!=1:errors.append(f'{p}: heading/title count {c.h1}/{c.titles}')
expected=['doceria-amorelli-experiencia','jjang-natal','loma-versao-original','loma-assessoria','nails2you-moema','ela-bella-esmalteria','valentina-marques-salao','dream-home-finder-000','perfumaria-deluxe','vic-franca-shop.myshopify.com','agenda-de-unha-conversa','sistemacypk.2.25.228.26.sslip.io','agendadeunha.com.br']
combined=''.join(p.read_text() for p in pages)
for term in expected:
 if term not in combined:errors.append('Missing project '+term)
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(pages)} HTML documents; {count} local asset/route references; all 13 supplied URLs; headings and alt text.')
