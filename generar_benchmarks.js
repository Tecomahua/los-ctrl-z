const fs=require('node:fs');
const path=require('node:path');
const root=__dirname;
function write(name,lines) {
  const fd=fs.openSync(path.join(root,name),'w');
  let buf='';
  for(const line of lines) {
    buf+=line;
    if(buf.length>1<<20) {fs.writeSync(fd,buf);buf='';}
  }
  if(buf) fs.writeSync(fd,buf);
  fs.closeSync(fd);
}
function* a1() {
  const n=4000000;
  yield `${n} 1 ${n} 1\n`;
  for(let i=0;i<n;i++) yield '1'+(i+1===n?'\n':' ');
}
function* a2() {
  const n=200000,m=400000;
  yield `${n} ${m}\n1 1 1 ${n}\n`;
  for(let i=1;i<n;i++) yield `${i} ${i+1} 40000000000000\n`;
  for(let i=0;i<m-n+1;i++) yield `1 1 1\n`;
}
function* a1mixed() {
  const n=4000000;
  yield `${n} 123 2345678 5\n`;
  for(let i=0;i<n;i++) yield [0,1,9,3,7,0,8][i%7]+(i+1===n?'\n':' ');
}
function* a2mixed() {
  const n=200000,m=400000;
  yield `${n} ${m}\n1 ${n} 12345 187654\n`;
  for(let i=1;i<n;i++) yield `${i} ${i+1} ${1+i%17}\n`;
  for(let i=0;i<m-n+1;i++) {
    const a=1+((Math.imul(i+1,7919)>>>0)%n);
    const b=1+((Math.imul(i+1,104729)>>>0)%n);
    yield `${a} ${b} ${1+i%1000}\n`;
  }
}
write('a1_benchmark.in',a1());
write('a2_benchmark.in',a2());
write('a1_mixed.in',a1mixed());
write('a2_mixed.in',a2mixed());
