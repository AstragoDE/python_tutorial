import{d as _,i as d,a as p,u as h,b as u,c as m,e as g,f as n,g as t,t as s,h as a,F as f,r as v,n as x,j as y,o as i,k as b,l as N,m as k,p as P,q as S,_ as w}from"./index-67fbc016.js";import{N as V}from"./NoteDisplay-6f10d8bb.js";const j={class:"m-4"},D={class:"mb-10"},H={class:"text-4xl font-bold mt-2"},L={class:"opacity-50"},T={class:"text-lg"},B={class:"font-bold flex gap-2"},C={class:"opacity-50"},F=t("div",{class:"flex-auto"},null,-1),z={key:0,class:"border-gray-400/50 mb-8"},A=_({__name:"PresenterPrint",setup(E){d(p),h(`
@page {
  size: A4;
  margin-top: 1.5cm;
  margin-bottom: 1cm;
}
* {
  -webkit-print-color-adjust: exact;
}
html,
html body,
html #app,
html #page-root {
  height: auto;
  overflow: auto !important;
}
`),u({title:`Notes - ${m.title}`});const r=g(()=>y.map(o=>{var l;return(l=o.meta)==null?void 0:l.slide}).filter(o=>o!==void 0&&o.noteHTML!==""));return(o,l)=>(i(),n("div",{id:"page-root",style:x(a(S))},[t("div",j,[t("div",D,[t("h1",H,s(a(m).title),1),t("div",L,s(new Date().toLocaleString()),1)]),(i(!0),n(f,null,v(a(r),(e,c)=>(i(),n("div",{key:c,class:"flex flex-col gap-4 break-inside-avoid-page"},[t("div",null,[t("h2",T,[t("div",B,[t("div",C,s(e==null?void 0:e.no)+"/"+s(a(b)),1),N(" "+s(e==null?void 0:e.title)+" ",1),F])]),k(V,{"note-html":e.noteHTML,class:"max-w-full"},null,8,["note-html"])]),c<a(r).length-1?(i(),n("hr",z)):P("v-if",!0)]))),128))])],4))}}),G=w(A,[["__file","F:/Programming/GitHub/AstragoDE_Sharing/python_tutorial/slides/node_modules/.pnpm/@slidev+client@0.42.5_postcss@8.4.27_vite@4.4.7/node_modules/@slidev/client/internals/PresenterPrint.vue"]]);export{G as default};
