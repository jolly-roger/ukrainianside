__gjsload_maps2__('poly', 'GAddMessages({});\'use strict\';var yW=function(a,b){return new y(a.o,a.j+b,!0)}; Hi.prototype.xI=Y(258,m("ri"));Ji.prototype.xI=Y(257,m("o"));Hi.prototype.uJ=Y(228,function(){dn(cn.ka(),w(function(){this.Va();this.Kr()}, this))}); Ji.prototype.uJ=Y(227,function(){dn(cn.ka(),w(function(){this.Va();this.Kr()}, this))}); Hi.prototype.Qz=Y(73,m("M"));Ji.prototype.Qz=Y(72,m("M"));var zW=function(a,b){return yW(a,zg((b.j-a.j)/360)*360)}, IVa=function(a,b,c,d,e){b=b.x+(c-b.y)/(a.y-b.y)*(a.x-b.x);if(b<=e&&b>=d)a.x=zg(b),a.y=c}, JVa=function(a,b,c,d,e){b=b.y+(c-b.x)/(a.x-b.x)*(a.y-b.y);if(b<=e&&b>=d)a.x=c,a.y=zg(b)}, KVa=function(a,b,c,d,e,f){a.x>d&&JVa(a,b,d,e,f);a.x<c&&JVa(a,b,c,e,f);a.y>f&&IVa(a,b,f,c,d);a.y<e&&IVa(a,b,e,c,d)}, LVa=function(a){if(a.jc())return new fp;else{var b=a.Gh(),a=a.Fh();return new fp(b,a)}}, AW,BW=function(a,b){return a.x*b.x+a.y*b.y};var MVa=function(a,b){var c=0,d=0,e=255;try{a.charAt(0)=="#"&&(a=a.substring(1)),c=parseInt(a.substring(0,2),16),d=parseInt(a.substring(2,4),16),e=parseInt(a.substring(4,6),16)}catch(f){}return c+","+d+","+e+","+(1-b)*255}, NVa=function(a,b,c,d,e,f,g,j,k,l){for(var n=i,o=k,k="",r=i,t,A,z=!1;!z&&o<=a.Jt();++o){var B=a.Kr(o,l),I=B.vectors,B=B.bounds,S=C(I);if(S>0&&C(I[0]))for(var G=S=0,U=C(I);G<U;++G)S+=C(I[G]);if(!(S>900)){if(C(I)&&C(I[0])){A=[];G=0;for(U=C(I);G<U;G++)Rg(A,I[G]);I=A}B.minX-=d;B.minY-=d;B.maxX+=d;B.maxY+=d;A=rua(c,B);t=I;B=new H(A.minX,A.minY);G=new H(A.maxX,A.maxY);if(B.x==uc||B.y==uc)t="";else{for(var U=[],S=i,J=0;J<C(t);J+=4){var da=new H(t[J],t[J+1]),T=new H(t[J+2],t[J+3]);da.equals(T)||(G&&(KVa(da, T,B.x,G.x,B.y,G.y),KVa(T,da,B.x,G.x,B.y,G.y)),da.equals(S)||(C(U)>0&&Nv(9999,U),Nv(da.x-B.x,U),Nv(da.y-B.y,U)),Nv(T.x-da.x,U),Nv(T.y-da.y,U),S=T)}Nv(9999,U);t=U.join("")}C(t)<=900&&(z=!0)}}t&&C(t)>0&&(k=tg(A.maxX-A.minX),c=tg(A.maxY-A.minY),k="http://mt.google.com/mld?width="+k+"&height="+c+"&path="+t,d&&e&&(k+="&color="+MVa(e,f)+"&weight="+d),g&&(k+="&fill="+MVa(g,j)),r=new H(A.minX,A.minY));f=I;d=r;e=k;if(C(e)>0)a=ua(D,a,"polyrasterloaded"),n=new Fi,n.alpha=!0,n.onLoadCallback=a,n=oq(e,b,d,i,n), bta()&&Wl(n);n?Yl(n,1E3):f=i;return{Y:n,jz:f}};var OVa=function(){if(!AW)AW=new cn,AW.o=!0;return AW}, PVa=function(a){var b=a.Tq,c=new H(b.maxX,b.minY);return new fp(a.Rb(new H(b.minX,b.maxY),!0),a.Rb(c,!0))}; Gi.prototype.Kr=function(a,b){var c=a||this.jt(),d=this.H;d.getSize();var e=PVa(d);this.K[c]||(this.K[c]={});var f=this.K[c];if(b||!f.cF||!f.cF.uk(e)){this.Bx=this.qm.expandBounds(so(d));var e=this.Bx.min(),g=this.Bx.max(),j=(e.x+g.x)/2,e=[e,g,new H(j,g.y),new H(j,e.y)];f.cF=new fp;F(e,function(a){f.cF.extend(Gw(d,a,!0))}); f.vectors=[];f.bounds=new vh;this.i_(c)}return f}; Gi.prototype.remove=function(){if(!this.xi)this.xi=!0,Jn(this),dn(OVa(),w(function(){this.eF()&&D(this,Oa)}, this))}; Gi.prototype.redraw=function(a,b){if(!this.Ua){if(a)this.dg=!0;var c=Jn(this);dn(OVa(),w(function(){if(c.xb()&&this.va){var a=this.dg;if(!this.xi){this.H.getSize();PVa(this.H);var e=so(this.H);if(a||!this.Bx||!this.Bx.uk(e))Qm(b,"plyrs"),this.eF(),this.Bx=this.qm.expandBounds(e),this.Y=this.qm.tu(this,a).Y,(a=this.getElement())&&this.qm&&this.qm.Ob(a,this.va),D(this,"redraw",this.Y),Qm(b,"plyrd")}this.dg=!1}}, this),b)}};function CW(a,b,c){this.C=a;this.j=b;this.o=c;this.D=BW(b,a);this.G=BW(c,a)} var QVa=function(a,b,c){b=new H(b.x-a.x,b.y-a.y);c/=BW(b,b);if(c>=1)return i;c=Math.sqrt(c/(1-c));return new CW(a,new H(b.x*c-b.y,b.y*c+b.x),new H(b.x*c+b.y,b.y*c-b.x))}; CW.prototype.contains=function(a){return BW(this.j,a)>=this.D&&BW(this.o,a)>=this.G}; var RVa=function(a,b){var c=new H(-b.y,b.x),d=BW(c,a.j),c=BW(c,a.o);if(d>=0&&c>=0)a.o=b,a.G=BW(b,a.C);else if(d<=0&&c<=0)a.j=b,a.D=BW(b,a.C)}; CW.prototype.toString=function(){for(var a=Math.atan2(-this.j.x,this.j.y)*180/Math.PI,b=Math.atan2(this.o.x,-this.o.y)*180/Math.PI;b<a;)b+=360;return"pt:"+this.C.toString()+" arc:["+a+","+b+"]"}; CW.prototype.Zd=m("C");var SVa=function(a,b,c){function d(a){l=b[g(a)];k.push(g(a));n=0} var e=i;a*=a;var f=0.95*a,g=c?function(a){return c[a]}:ba(), j=c?C(c):C(b);if(j<2)return[];var k=[],l,n;d(0);for(var o=1;o<j;++o){var r=b[g(o)],t=Vfa(l,r);t<=a||(!e||!e.contains(r)||t<n?(o>1&&d(o-1),e=QVa(l,r,f)):(n=t,r=QVa(l,r,f),RVa(e,r.j),RVa(e,r.o)))}d(j-1);return k}, TVa=function(a,b){for(var c=Array(C(a)),d=0,e=C(a);d<e;++d)c[d]=0;for(var f=i,d=0,e=C(b);d<e;++d)for(var f=SVa(b[d],a,f),g=0,j=C(f);g<j;++g)++c[f[g]];return c};var DW=function(a,b,c,d,e,f){var g=-1;b!=i&&(g=0);c!=i&&(g=1);d!=i&&(g=2);e!=i&&(g=3);if(g==-1)return[];for(var j=i,k=[],l=0;l<C(a);l+=2){var n=a[l],o=a[l+1];if(!(n.x==o.x&&n.y==o.y)){var r,t;switch(g){case 0:r=n.y>=b;t=o.y>=b;break;case 1:r=n.y<=c;t=o.y<=c;break;case 2:r=n.x>=d;t=o.x>=d;break;case 3:r=n.x<=e,t=o.x<=e}if(r||t)if(r&&t)k.push(n),k.push(o);else{var A;switch(g){case 0:A=n.x+(b-n.y)*(o.x-n.x)/(o.y-n.y);A=new y(b,A,!0);break;case 1:A=n.x+(c-n.y)*(o.x-n.x)/(o.y-n.y);A=new y(c,A,!0);break; case 2:A=n.y+(d-n.x)*(o.y-n.y)/(o.x-n.x);A=new y(A,d,!0);break;case 3:A=n.y+(e-n.x)*(o.y-n.y)/(o.x-n.x),A=new y(A,e,!0)}r?(k.push(n),k.push(A),j=A):t&&(j&&(k.push(j),k.push(A),j=i),k.push(A),k.push(o))}}}f&&j&&(k.push(j),k.push(k[0]));return k}, UVa=function(a,b,c,d,e){for(var f=i,g=C(a),j=0;j<g;++j)f=e(a[(j+d)%g]),b.push(zg(f.x)),b.push(zg(f.y)),c.extend(f)}; Hi.prototype.i_=function(a){var b=this.H,b=w(b.Mk,b),c=this.K[a],a=this.Ze(c.cF,a);UVa(a,c.vectors,c.bounds,this.cr(a),b)}; var ZVa=function(a,b,c,d){b instanceof Ca&&(b=LVa(b));var e=VVa(a);e.xa();if(b)var f=tg((b.Qm()-e.Pl())/360),e=vg((b.Pl()-e.Qm())/360);else e=f=0;d||(b=i);v(a.J)||a.IF();for(d=[];f<=e;++f){var g=yW(a.Z[0],360*f),j=[];WVa(a,b,0,C(a.Z)-1,a.o-1,c,j,g);if(a.Ra){var k=a.H.W(),l=a.H.ia().ic(),g=function(a){return l.pd(a,k)}, n=Tg(j);$g(j);for(var o=0,r=C(n);o<r;o+=2)for(var t=XVa([n[o],n[o+1]],g,a.weight,b),A=0,z=C(t);A<z;A+=2)YVa(j,b,t[A],t[A+1])}d.push(j)}return d}; Hi.prototype.Ze=function(a,b){for(var c=[],d=ZVa(this,a,b,!0),e=0,f=C(d);e<f;++e)Rg(c,d[e]);return c}; var $Va=function(a,b,c){var d=a.H.ia().ic(),e=d.pd(b.Gh(),17),b=d.pd(b.Fh(),17),a=a.V*Math.pow(a.O,c),e=new H(e.x-a,e.y+a),b=new H(b.x+a,b.y-a),e=d.bh(e,17,!0),b=d.bh(b,17,!0);return new fp(e,b)}, WVa=function(a,b,c,d,e,f,g,j){var k=i;b&&(k=$Va(a,b,e));for(var j=zW(a.Z[c],j),l=a.KE(c,e);l<=d;){var n=zW(a.Z[l],j),o=a.Ra?xs([j,n]):new fp(j,n);if(k==i||k.intersects(o))e>f?WVa(a,b,c,l,e-1,f,g,j):YVa(g,a.Ra?i:k,j,n);j=n;c=l;e?l=a.KE(c,e):++l}}; function aWa(a){for(var b=0,c=0;c<C(a)-1;++c)b+=Gg(a[c+1].lng()-a[c].lng(),-180,180);return zg(b/360)} var bWa=function(a,b){var c=C(a.Z),d=Array(c),e=[];if(c)for(var f=new hp(b+1),g=a.Z[0],j=g.lng(),k=0;k<c;++k){var l=a.Z[k].lng(),n=l+360*zg((g.lng()-l)/360),l=n==l?a.Z[k]:new y(a.Z[k].lat(),n);d[k]=f.pd(l,b);rg(n-j)>=180&&(j=g.lng(),e.push(k-1));g=l}return{points:d,wW:e}}; q=Hi.prototype;q.IF=function(){var a=C(this.Z);if(a||!this.Ah)this.Wi=!0;if(a){var b=bWa(this,17),c=b.points,b=b.wW,d=Qg([0,1,2],function(a){return 3*(1<<4*a)}); this.j=TVa(c,d);this.o=4;c=0;for(d=C(b);c<d;++c)this.j[b[c]]=3;this.J=Bs(this.j,this.o)}else this.j=[],this.J=[];if(a>0&&this.Z[0].equals(this.Z[a-1]))this.Ka=aWa(this.Z)}; q.v_=function(a,b){if(C(this.Z)==0)return i;for(var c=bWa(this,b),d=c.wW,c=SVa(a,c.points),c=c.concat(d).sort(function(a,b){return a-b}), d=[],e=0;e<c.length;++e)(e==0||c[e]!=c[e-1])&&d.push(this.Z[c[e]]);return new Hi(d)}; q.KE=function(a,b){for(var c=this.j,d=C(c),e=this.J,f=a+1;f<d&&c[f]<b;)f=e[f];return f}; q.wS=function(a){if(this.pe()&&this.va!=a)(this.va=a)&&this.redraw(!1),this.qm&&this.qm.Ob(this.getElement(),a),D(this,Qa,a)}; q.GI=function(a,b){var c=this.H,d=this.Kr().vectors;if(!d||!c)return i;if(this.Q.vectors!=d)this.Q.vectors=d,this.Q.iP=EW(d,0,C(d));var e=this.Q.iP,c=c.Mk(a),f=FW(this,b),g=new vh(c.x-f,c.y-f,c.x+f,c.y+f);return GW(e,d,c,g,f)}; function GW(a,b,c,d,e){var f=i;if(Hz(a.bounds,d))if(a.leaf)for(d=a.start;d<a.start+a.len;d+=4){var g,j=b[d];g=b[d+1];var k=b[d+2]-j,l=b[d+3]-g,n=c.x-j,o=c.y-g,r=k*k+l*l,t=0;r!=0&&(t=(k*n+l*o)/r);t<0?t=0:t>1&&(t=1);j+=k*t;g+=l*t;l=(j-c.x)*(j-c.x)+(g-c.y)*(g-c.y);t=i;l<e*e&&(t={point:new H(j,g),distSq:l});if((g=t)&&(!f||g.distSq<f.distSq))f=g,f.segmentIndex=d/4}else f=GW(a.a,b,c,d,e),a=GW(a.b,b,c,d,e),f=!f||a&&a.distSq<f.distSq?a:f;return f} function YVa(a,b,c,d){if(!(c.lat()==d.lat()&&c.lng()==d.lng()))if(b==i||b.contains(c)&&b.contains(d))a.push(c),a.push(d);else{var c=yW(c,0),d=yW(d,0),e=b.Nn(),f=b.To(),g=b.Pl(),b=b.Qm(),c=[c,d],c=DW(c,e,i,i,i,!1),c=DW(c,i,f,i,i,!1),c=DW(c,i,i,b,i,!1),c=DW(c,i,i,i,g,!1);Rg(a,c)}} var FW=function(a,b){var c=Math.ceil(2.5);return wg(b||c,zg(a.weight/2))}; q=Hi.prototype;q.hP=function(a){var b=this.H,c=b.W();if(!this.qr)this.qr=[];var d=this.qr[c];if(!d){d=this.Va();if(!d)return i;var a=FW(this,a),e=b.yb(d.Gh()),d=b.yb(d.Fh()),d=new Ca(b.Rb(new H(e.x-a,e.y+a)),b.Rb(new H(d.x+a,d.y-a)));this.qr[c]=d}return d}; q.jt=function(){if(this.Wi)return 0;else{var a=17-this.H.W(),a=this.V*Math.pow(2,-a),b=0;do++b,a*=this.O;while(b<this.o&&a<=1);return b-1}}; q.cr=function(a){if(!a||C(a)==0)return 0;if(!a[0].equals(ew(a)))return 0;if(this.Ka==0)return 0;for(var b=this.H.xa(),c=0,d=0,e=0;e<C(a);e+=2){var f=Gg(a[e].lng()-b.lng(),-180,180)*this.Ka;f<d&&(d=f,c=e)}return c}; function EW(a,b,c){if(c<=40){for(var d=new vh,e=b;e<b+c;e+=4)d.extend(new H(a[e],a[e+1])),d.extend(new H(a[e+2],a[e+3]));a={leaf:!0,start:b,len:c,bounds:d}}else d=vg(c/8)*4,e=EW(a,b,d),a=EW(a,b+d,c-d),d=new vh,d.extend(e.bounds.min()),d.extend(e.bounds.max()),d.extend(a.bounds.min()),d.extend(a.bounds.max()),a={leaf:!1,a:e,b:a,bounds:d};return a} q.Tt=function(a,b){var c;c=i;var d=this.GI(a,b||10);if(d)c={},c.yq=Bg(d.distSq),c.bd=d.point,c.Sa=d.segmentIndex;return!c?i:c.yq<FW(this,b)?c:i}; q.b_=function(a,b){this.Y=NVa(this,a,this.Bx,this.weight,this.color,this.opacity,"",0,this.jt(),b).Y}; q.eF=function(){return this.Y?(this.qm.kl(this.Y),this.Y=i,this.K={},this.Q={},!0):!1}; var VVa=function(a){var b=new fp,c=C(a.Z);if(!c)return b;for(var d=a.Z[0],e=wg(a.o-1,0),f=0;f<c;f=a.KE(f,e))d=zW(a.Z[f],d),b.extend(d);return e?$Va(a,b,e):b}; delete Hi.prototype.redraw;delete Hi.prototype.remove;q=Ji.prototype;q.i_=function(a){var b=this.H,b=w(b.Mk,b),c=this.K[a],d=c.cF;d instanceof Ca&&(d=LVa(d));for(var e=[],f=0;f<C(this.ib);++f)Rg(e,cWa(this.ib[f],d,a));a=0;for(d=C(e);a<d;++a){var g=e[a],j=[],f=new vh;UVa(g,j,f,0,b);c.vectors.push(j);g=c.bounds;if(!f.jc())g.minX=xg(g.minX,f.minX),g.maxX=wg(g.maxX,f.maxX),g.minY=xg(g.minY,f.minY),g.maxY=wg(g.maxY,f.maxY)}}; function cWa(a,b,c){var a=ZVa(a,b,c,!1),d=[],e=b.Nn(),f=b.To(),g=b.Pl(),j=b.Qm();F(a,function(a){a=DW(a,e,i,i,i,!0);a=DW(a,i,f,i,i,!0);a=DW(a,i,i,j,i,!0);a=DW(a,i,i,i,g,!0);d.push(a)}); return d} q.vS=function(a){if(this.pe()&&this.va!=a){this.va=a;var b=this.getElement();a&&this.redraw(!1);this.qm&&this.qm.Ob(b,a);if(!this.Ja&&!(cy()||Wy()?0:M.type!=1||!dy())||!b){for(b=0;b<C(this.ib);++b)a?this.ib[b].show():this.ib[b].hide();D(this,Qa,a)}}}; q.HY=function(a){var b=this.H.W(),c=this.qr[b];if(!c){for(var c=new Ca,d=0;d<this.ib.length;++d){var e=this.ib[d].hP(a);e!=i&&c.union(e)}this.qr[b]=c}return c}; q.oP=function(a){var b=this.H,c=this.Kr().vectors;if(!c||!b)return i;var d;if(this.j.vectors!=c)d=ah(c),this.j.vectors=c,this.j.Kaa=d,this.j.iP=EW(d,0,C(d));d=this.j.Kaa;c=this.j.iP;a=b.Mk(a);return!!(HW(c,d,a)%2)}; function HW(a,b,c){var d=0;if(a.bounds.maxX>=c.x&&a.bounds.minY<=c.y&&a.bounds.maxY>=c.y)if(a.leaf)for(var e=c.x,c=c.y,f=a.start;f<a.start+a.len;){var g=b[f++],j=b[f++],k=b[f++],l=b[f++];if(l<j)var n=g,g=k,k=n,n=j,j=l,l=n;j<=c&&c<l&&(e-g)*(l-j)<(c-j)*(k-g)&&++d}else d+=HW(a.a,b,c),d+=HW(a.b,b,c);return d} q.jt=function(){for(var a=100,b=0;b<C(this.ib);++b){var c=this.ib[b].jt();a>c&&(a=c)}return a}; q.Tt=function(a,b){return this.ib[0].Tt(a,b)}; q.b_=function(a,b){var c="",d=0;if(this.fill)c=this.color,d=this.opacity;for(var e=0,f=C(this.ib);e<f;++e){var g=this.ib[e],j=0;if(this.outline)j=g.weight;j=NVa(this,a,this.Bx,j,g.color,g.opacity,c,d,g.jt(),b);g.Y=j.Y}}; q.eF=function(){for(var a=!1,b=0;b<C(this.ib);++b)this.ib[b].Y&&(a=!0),this.ib[b].remove();if(this.Y)a=!0,this.qm.kl(this.Y),this.Y=i,this.K={},this.j={};return a}; delete Ji.prototype.redraw;delete Ji.prototype.remove;function XVa(a,b,c,d){b=new dWa(b,c,d);c=[];c[0]=new zs(a[0]);gp(c[0].latlng,c[0].r3);c[1]=new zs(a[1]);gp(c[1].latlng,c[1].r3);a=IW(b,c,0);b=[];c=0;for(d=C(a);c<d;++c)b.push(a[c].latlng);return b} function dWa(a,b,c){this.SJ=a;a=b||0;a<3&&(a=3);this.j=a;this.Ne=c||i} var IW=function(a,b,c){if(c>10)return b;var d=xs([b[0].latlng,b[1].latlng]);if(a.Ne&&!d.intersects(a.Ne))return[];var e=a.SJ(b[0].latlng),f=a.SJ(b[1].latlng),d=new zs;if(!JW(b,d))return b;a.SJ(d.latlng);for(var g=[],j=1;j<4;++j){var k=j/4;g.push(new H(e.x*(1-k)+f.x*k,e.y*(1-k)+f.y*k))}var l=[];l[0]=new zs;if(!JW([b[0],d],l[0]))return b;l[1]=d;l[2]=new zs;if(!JW([d,b[1]],l[2]))return b;F(l,w(function(a,b){l[b]=this.SJ(a.latlng)}, a));e=!1;for(j=0;j<3;++j)if(f=g[j],k=l[j],!(rg(f.x-k.x)<a.j&&rg(f.y-k.y)<a.j)){e=!0;break}return e?(g=[d,b[1]],b=IW(a,[b[0],d],c+1),a=IW(a,g,c+1),Rg(b,a),b):b}; function JW(a,b){b.r3[0]=(a[0].r3[0]+a[1].r3[0])/2;b.r3[1]=(a[0].r3[1]+a[1].r3[1])/2;b.r3[2]=(a[0].r3[2]+a[1].r3[2])/2;var c=b.r3,d=Bg(c[0]*c[0]+c[1]*c[1]+c[2]*c[2]);c[0]/=d;c[1]/=d;c[2]/=d;Vja(b.r3,b.latlng);c=xg(a[0].latlng.j,a[1].latlng.j);for(d=wg(a[0].latlng.j,a[1].latlng.j);b.latlng.j>d;)b.latlng.j-=360;for(;b.latlng.j<c;)b.latlng.j+=360;return b.latlng.j>d?!1:!0} ;Gs.ra=function(){this.ib=[];this.j=[];this.o=i}; q=Gs.prototype;q.x2=!0;q.initialize=ea("H");q.Ea=function(a,b,c){var d=a.vb();d=="Polyline"?this.ib.push(a):d=="Polygon"&&this.j.push(a);a.initialize(this.H,c);a.redraw(!0,b);(sz(a,E)||sz(a,Va))&&a.uJ();vo(this.H,a)}; q.Za=function(a){var b=a.vb();b=="Polyline"?Ig(this.ib,a):b=="Polygon"&&Ig(this.j,a);a.remove();wo(a)}; q.rQ=ea("x2");q.dS=function(a){var b=KW(this,a,Ua);b&&D(b,"opencontextmenu",0,a);return b}; q.Ap=function(a,b,c,d){if(b==eb&&d)return eWa(this,a,d);return b==E&&this.x2&&d&&(a=KW(this,d,b))?(D(a,E,d),!0):!1}; var KW=function(a,b,c){var d=Va;fb==c?d=gb:Ua==c?d=xb:eb==c&&(d=eb);if(a.ib)for(var e=C(a.ib)-1;e>=0;--e){var f=a.ib[e];if(!f.ub()&&f.Qz()&&(!c||sz(f,c)||sz(f,d))){var g=f.hP();if(g&&g.contains(b)&&f.Tt(b))return f}}if(a.j){for(var f=[],e=0,j=C(a.j);e<j;++e){var k=a.j[e];if(!k.ub()&&k.Qz()&&(!c||sz(k,c)||sz(k,d)))(g=k.HY())&&g.contains(b)&&f.push(k)}for(e=C(f)-1;e>=0;--e)if(k=f[e],k.ib[0].Tt(b))return k;for(e=C(f)-1;e>=0;--e)if(k=f[e],k.oP(b))return k}return i}, eWa=function(a,b,c){var d=a.o;if(!C(a.ib)&&!C(a.j))return!1;if(Xv){if(d&&!d.ai())d.Hr(),D(d,gb),a.o=i;return!1}if(Cs&&Cs())return!1;var e=KW(a,c,fb);d&&e!=d&&d.Tt(c,d.xI()||20)&&(e=d);if(d!=e){if(d)qn(zm(b),Jw(a.H.Pa())),D(d,gb,0),a.o=i;if(e)qn(zm(b),e.Qz()?"pointer":"default"),a.o=e,D(e,fb,0)}return(e=KW(a,c,fb))?(D(e,eb,0,c),!0):!1};W("poly",2);W("poly",3);W("poly",4,Gs);W("poly");', '', []);