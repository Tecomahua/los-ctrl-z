const { spawnSync } = require('node:child_process');
const path = require('node:path');
const root = __dirname;
let seed = 20261105;
function rnd(max) { seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0; return seed % max; }
function run(name, input) {
  const p = spawnSync(path.join(root, name), { input, encoding: 'utf8' });
  if (p.status !== 0) throw Error(`${name}: exit=${p.status}, stderr=${p.stderr}`);
  return p.stdout.trim();
}
function a1ref(a, L, R, M) {
  let count = 0, lengths = 0;
  for (let i = 0; i < a.length; i++) for (let j = i; j < a.length; j++) {
    const len = j - i + 1;
    if (len < L || len > R) continue;
    const v = a.slice(i, j + 1).filter(x => x !== 0).sort((x,y) => x-y);
    if (v.length && v[Math.floor(v.length / 2)] >= M) { count++; lengths += len; }
  }
  return `${count} ${lengths}`;
}
function checkA1(a,L,R,M,expected=a1ref(a,L,R,M)) {
  const input = `${a.length} ${L} ${R} ${M}\n${a.join(' ')}\n`;
  const got=run('a1_test.exe',input);
  if(got!==expected) throw Error(`A1 mismatch input=${JSON.stringify(input)} got=${got} expected=${expected}`);
}
function dists(n,edges,source) {
  const d=Array(n).fill(Infinity); d[source]=0;
  for(let k=0;k<n;k++) {
    let changed=false;
    for(const [a,b,w] of edges) {
      if(d[a]+w<d[b]) {d[b]=d[a]+w;changed=true;}
      if(d[b]+w<d[a]) {d[a]=d[b]+w;changed=true;}
    }
    if(!changed) break;
  }
  return d;
}
function a2ref(n,edges,S,T,U,V) {
  const ds=dists(n,edges,S), du=dists(n,edges,U), dv=dists(n,edges,V);
  let ans=du[V];
  if(Number.isFinite(ds[T])) {
    const used=Array(n).fill(false), path=[S]; used[S]=true;
    function visit(a,cost) {
      if(a===T) {
        if(cost===ds[T]) for(let i=0;i<path.length;i++) for(let j=i;j<path.length;j++)
          ans=Math.min(ans,du[path[i]]+dv[path[j]]);
        return;
      }
      for(const [x,y,w] of edges) {
        const b=x===a?y:y===a?x:-1;
        if(b>=0 && !used[b] && cost+w<=ds[T]) {
          used[b]=true;path.push(b);visit(b,cost+w);path.pop();used[b]=false;
        }
      }
    }
    visit(S,0);
  }
  return Number.isFinite(ans)?`${ans}`:'-1';
}
function checkA2(n,edges,S,T,U,V,expected=a2ref(n,edges,S,T,U,V)) {
  const input=`${n} ${edges.length}\n${S+1} ${T+1} ${U+1} ${V+1}\n`+
    edges.map(([a,b,w])=>`${a+1} ${b+1} ${w}`).join('\n')+'\n';
  const got=run('a2_test.exe',input);
  if(got!==expected) throw Error(`A2 mismatch input=${JSON.stringify(input)} got=${got} expected=${expected}`);
}
let a1=0,a2=0;
checkA1([2,1,4,2,2,5,6],3,7,2,'15 65');a1++;
checkA1([4,2,5,5,2,4,6,1,6],5,9,3,'15 95');a1++;
for(let t=0;t<300;t++) {
  const n=1+rnd(10), a=Array.from({length:n},()=>rnd(7));
  const L=1+rnd(n),R=L+rnd(n-L+1),M=1+rnd(7);
  checkA1(a,L,R,M);a1++;
}
checkA2(4,[[3,0,7],[1,3,8],[0,0,3],[2,3,9],[3,1,7]],3,1,2,1,'9');a2++;
checkA2(4,[[1,2,2],[0,2,1],[3,1,3],[3,0,1],[3,1,2],[3,3,3],[1,3,2],[1,1,1]],2,3,0,1,'2');a2++;
for(let t=0;t<300;t++) {
  const n=1+rnd(7),m=rnd(14),edges=[];
  for(let i=0;i<m;i++) edges.push([rnd(n),rnd(n),1+rnd(9)]);
  checkA2(n,edges,rnd(n),rnd(n),rnd(n),rnd(n));a2++;
}
console.log(`A1 ${a1}/${a1}; A2 ${a2}/${a2}; seed=20261105`);
