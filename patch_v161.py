# -*- coding: utf-8 -*-
import io
P='/tmp/ibrepo/index.html'
src=io.open(P,encoding='utf-8').read()
def rep(old,new,tag):
    global src
    c=src.count(old)
    assert c==1, 'ANCHOR[%s] count=%d' % (tag,c)
    src=src.replace(old,new,1)
    print('OK R[%s]' % tag)

# ── R1: _xcRenderSnapshot 支持外部容器 ──
rep("function _xcRenderSnapshot(s){/* v158-p: 心绪面板——官方前端内容本地化 · IB 风格 */\n    const box=document.getElementById('xcm-snap-panel');if(!box)return;box.style.display='block';",
    "function _xcRenderSnapshot(s,box2){/* v158-p: 心绪面板——官方前端内容本地化 · IB 风格 */\n    const box=box2||document.getElementById('xcm-snap-panel');if(!box)return;box.style.display='block';",
    'R1-xcRender-box2')

# ── R2: _xcRenderSnapshot window 桥（v161-p：视界驾驶舱跨模块复用） ──
rep("+(dreams.length?'<div style=\"margin-top:8px;font-size:0.72rem;color:var(--tx2)\">最近梦境：'+dreamTxt+'</div>':'');\n  }\n})();",
    "+(dreams.length?'<div style=\"margin-top:8px;font-size:0.72rem;color:var(--tx2)\">最近梦境：'+dreamTxt+'</div>':'');\n  }\n  window._xcRenderSnapshot=_xcRenderSnapshot;/* v161-p：跨模块桥——视界驾驶舱复用快照渲染 */\n})();",
    'R2-xcRender-bridge')

# ── R3: _ibMemWriteExecM —— OB Only（本地库下线） ──
rep("try{await dbPut('memories',mem)}catch(e){return{ok:false,reason:'写入本地数据库失败'}}\n_ibEmbedMemAsync(mem);/* v154-p：写入后异步向量化（不阻塞回复） */\n  if(_xcoOn())_xcoHoldDefer(mem);/* v160-p：心潮念 OB 中继（异步，不阻塞） */\n  try{if(document.querySelector('#page-memory.active'))renderMemLib()}catch(e){}\n  return{ok:true,label:'已写入记忆库 ·「'+title+'」',response:'已写入（仅自己可见；用户可在 Memory 页查看与编辑）。'};",
    "if(_xcoOn()){/* v161-p：OB Only——本地记忆库下线，写入直达心潮念（同步确认） */\n    let _hro9=null;\n    try{_hro9=await _xcoHold(mem)}catch(e){}\n    if(_hro9&&_hro9.ok)return{ok:true,label:'已写入心潮念 ·「'+title+'」',response:'已写入（OB接管：仅同步至心潮念，本地记忆库已下线）。'};\n    return{ok:false,reason:'心潮念写入失败：'+((_hro9&&_hro9.reason)||'网关不可达')};\n  }\n  try{await dbPut('memories',mem)}catch(e){return{ok:false,reason:'写入本地数据库失败'}}\n  _ibEmbedMemAsync(mem);/* v154-p：写入后异步向量化（不阻塞回复） */\n  try{if(document.querySelector('#page-memory.active'))renderMemLib()}catch(e){}\n  return{ok:true,label:'已写入记忆库 ·「'+title+'」',response:'已写入（仅自己可见；用户可在 Memory 页查看与编辑）。'};",
    'R3-ibMemWrite-OBOnly')

# ── R4: _vzAllMems —— OB Only（无本地回退） ──
rep("if(_xcoOn()){/* v160-p：OB 全量目录优先 */\n    return _xcoBuckets().then(function(a){var m=_xcoMapBuckets(a);if(m&&m.length){_vzCache.mems=m;return m}return _vzLocalAll()}).catch(function(){return _vzLocalAll()});\n  }",
    "if(_xcoOn()){/* v161-p：OB Only——目录仅来自心潮念，不回退本地 */\n    return _xcoBuckets().then(function(a){var m=_xcoMapBuckets(a);_vzCache.mems=m||[];return _vzCache.mems}).catch(function(){_vzCache.mems=[];return _vzCache.mems});\n  }",
    'R4-vzAllMems-OBOnly')

# ── R5: _renderViz 尾调用驾驶舱刷新 ──
rep("mems.length+' 条记忆</span>';\n    _vzHeat();\n  });\n}",
    "mems.length+' 条记忆</span>';\n    _vzHeat();\n    _vizXcRender();/* v161-p：心潮驾驶舱随视界刷新 */\n  });\n}",
    'R5-renderViz-tail')

# ── R6: navTo 尾部 —— 全局跳转钩子 + Chat 侧栏注入 ──
rep("  renderDock();\n  showSec();\n  window.scrollTo(0,0);\n}",
    """  renderDock();
  showSec();
  window.scrollTo(0,0);
}
/* ═══ v161-p：心潮视界驾驶舱——无缝跳转 / 原位返回（全局钩子） ═══ */
window._vzNavBack={sec:'list',convOpen:false};
window._xzJump=function(){
  try{
    var cv=document.getElementById('conv');
    window._vzNavBack.sec=(typeof _sec!=='undefined'&&_sec&&_sec.chat)||'list';
    window._vzNavBack.convOpen=!!(cv&&cv.classList.contains('open'));
    if(cv)cv.classList.remove('open');
    if(document.body.classList.contains('on-conv'))document.body.classList.remove('on-conv');
    try{_sec.memory='viz'}catch(e){}
    navTo('memory');
  }catch(e){}
};
window._xzJumpBack=function(){
  try{
    var cv=document.getElementById('conv');
    navTo('chat');
    try{if(window._vzNavBack.sec)_sec.chat=window._vzNavBack.sec}catch(e){}
    if(cv&&window._vzNavBack.convOpen){cv.classList.add('open');document.body.classList.add('on-conv')}
  }catch(e){}
};
(function(){/* Chat 侧栏注入「视界 · 心潮驾驶舱」入口 */
  try{
    var ops=document.getElementById('cs-ops');if(!ops||document.getElementById('cs-viz-jump'))return;
    var it=document.createElement('div');it.className='cs-item';it.id='cs-viz-jump';
    it.innerHTML='<svg viewBox="0 0 24 24"><path d="M3 12h4l2.5-6 4 10 2.5-4H21"/></svg><span><b class="cs-cn">视界 · 心潮驾驶舱</b></span>';
    it.addEventListener('click',function(){
      try{var cs=document.getElementById('chat-side');if(cs)cs.classList.remove('open')}catch(e){}
      if(window._xzJump)window._xzJump();
    });
    ops.insertBefore(it,ops.firstChild);
  }catch(e){}
})();""",
    'R6-navTo-jsbridge')

# ── R7: 视界 IIFE —— 驾驶舱实现 ──
rep("SEC_RENDER['memory:viz']=_renderViz;",
    """SEC_RENDER['memory:viz']=_renderViz;

/* ═══ v161-p：心潮视界驾驶舱——感知心潮念实时心智（驱力/梦境）+ OB 记忆接管 ═══ */
function _vizXcEnsure(){/* 注入驾驶舱 DOM（幂等） */
  var wrap=document.getElementById('viz-xc-cockpit');
  if(wrap)return wrap;
  var hero=document.querySelector('#sec-memory-viz .viz-hero');
  if(!hero)return null;
  wrap=document.createElement('div');wrap.id='viz-xc-cockpit';
  wrap.innerHTML=
    '<div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin:14px 2px 0">'
    +'<div class="sec-label" style="margin:0;flex:1">心潮驾驶舱<span id="viz-xc-live" style="margin-left:8px;font-size:0.7rem;color:var(--tx3);letter-spacing:0"></span></div>'
    +'<button class="btn" id="viz-xc-back" style="flex:0 0 auto;padding:6px 12px">← 返回对话</button></div>'
    +'<div class="card"><div id="viz-xc-body"><p class="hint">驾驶舱装载中…</p></div></div>'
    +'<div class="sec-label" id="viz-xc-dream-label" style="display:none">梦境时序流</div>'
    +'<div class="card" id="viz-xc-dream-card" style="display:none"><div id="viz-xc-dreams"></div></div>'
    +'<div class="sec-label" id="viz-xc-ob-label" style="display:none">心潮念 · 记忆接管</div>'
    +'<div class="card" id="viz-xc-ob-card" style="display:none"><div id="viz-xc-ob"></div></div>';
  hero.parentNode.insertBefore(wrap,hero.nextSibling);
  var bk=document.getElementById('viz-xc-back');
  if(bk)bk.addEventListener('click',function(){if(window._xzJumpBack)window._xzJumpBack()});
  return wrap;
}
function _vizDreamFlow(s){/* 梦境时序流（时间倒序） */
  var lab=document.getElementById('viz-xc-dream-label'),card=document.getElementById('viz-xc-dream-card'),box=document.getElementById('viz-xc-dreams');
  if(!lab)return;
  var dreams=Array.isArray(s&&s.dreams)?s.dreams.slice():[];
  if(!dreams.length){lab.style.display='none';if(card)card.style.display='none';return}
  dreams.sort(function(a,b){return new Date(b&&b.createdAt||0)-new Date(a&&a.createdAt||0)});
  dreams=dreams.slice(0,8);
  lab.style.display='';if(card)card.style.display='';
  var rows=dreams.map(function(d,i){
    var ts=(d&&d.createdAt)?String(d.createdAt).slice(0,16).replace('T',' '):'--';
    var luc=Math.round((Number(d&&d.lucidity)||0)*100);
    var sum=String((d&&(d.summary||d.title))||'');
    return '<div style="display:flex;align-items:center;gap:8px;margin:6px 0;font-size:0.76rem">'
      +'<span style="flex:0 0 96px;color:var(--tx3)">'+ts+'</span>'
      +'<span style="flex:0 0 46px;text-align:center;border:1px solid var(--line);border-radius:999px;padding:1px 0;color:var(--tx2)">清 '+luc+'%</span>'
      +'<span style="flex:1;color:var(--tx2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis" title="'+sum.replace(/"/g,'"')+'">'
      +(sum||'（无摘要）')+'</span></div>';
  }).join('');
  box.innerHTML='<div style="font-size:0.72rem;color:var(--tx3);margin:0 0 2px">按时间倒序 · 最近 '+dreams.length+' 条</div>'+rows;
}
function _vizXcRender(){/* 驾驶舱渲染——随视界刷新 */
  var wrap=_vizXcEnsure();if(!wrap)return;
  var xcOn=!!(typeof _xcCfg!=='undefined'&&_xcCfg&&_xcCfg.xc&&_xcCfg.xc.on&&_xcCfg.xc.base);
  var obOn=(typeof _xcoOn==='function')?_xcoOn():false;
  if(!xcOn&&!obOn){wrap.style.display='none';return}
  wrap.style.display='';
  var live=document.getElementById('viz-xc-live');
  if(live)live.textContent=(obOn?'OB接管·':'本地·')+new Date().toTimeString().slice(0,5);
  var body=document.getElementById('viz-xc-body');
  if(!xcOn){
    if(body)body.innerHTML='<p class="hint">尚未开启「心潮情绪」：API → 全局设置 → 记忆增强，填写服务地址并开启后即可感知驱力与梦境。</p>';
  }else{
    if(body)body.innerHTML='<p class="hint">正在感知心潮念…</p>';
    _xcFetchSnap().then(function(s){
      if(!s){if(body)body.innerHTML='<p class="hint">快照获取失败：请检查服务地址 / Token（需公网可达）。</p>';return}
      try{_xcSnap={t:Date.now(),line:_xcLineFrom(s),raw:s}}catch(e){}
      if(typeof window._xcRenderSnapshot==='function'){
        try{window._xcRenderSnapshot(s,body)}catch(e){if(body)body.innerHTML='<p class="hint">快照渲染异常：'+String(e&&e.message||e)+'</p>'}
      }else if(body){body.innerHTML='<p class="hint">渲染器未就绪（快照桥缺失）。</p>'}
      _vizDreamFlow(s);
    }).catch(function(){if(body)body.innerHTML='<p class="hint">快照获取失败（网络异常）。</p>'});
  }
  if(obOn){
    var obLab=document.getElementById('viz-xc-ob-label'),obCard=document.getElementById('viz-xc-ob-card'),obBox=document.getElementById('viz-xc-ob');
    if(obLab){obLab.style.display='';if(obCard)obCard.style.display=''}
    if(obBox){
      obBox.innerHTML='<p class="hint">正在读取心潮念目录…</p>';
      if(typeof _xcoBuckets==='function'){
        _xcoBuckets().then(function(a){
          var n=(a&&a.length)||0;
          obBox.innerHTML='<div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">'
            +'<span class="xcm-snap-tag">目录 '+n+' 条</span>'
            +'<span class="xcm-snap-tag">本地记忆库已下线</span></div>'
            +'<div style="margin-top:8px;font-size:0.72rem;color:var(--tx2)">'
            +((a||[]).slice(0,5).map(function(b){return String(b.name||b.title||'').slice(0,20)}).join('、')||'暂无条目')
            +'</div>';
        }).catch(function(){obBox.innerHTML='<p class="hint">OB 目录读取失败（网关不可达）。</p>'});
      }else if(obBox){obBox.innerHTML='<p class="hint">OB 客户端未就绪。</p>'}
    }
  }
}""",
    'R7-viz-cockpit')

# ── R8/R9: 版本 bump ──
rep("IB_VER='v151-p'", "IB_VER='v161-p'", 'R8-IBVER')
rep("<!-- InternalBeyond Mobile v145-p · 双层根修与低饱和重制轮（英雄区方框投影双层分离根修 / 相遇纪念卡低饱和「月光水银」重制 / MCP 浏览器版独立与边界整治） -->",
    "<!-- InternalBeyond Mobile v145-p · 双层根修与低饱和重制轮（英雄区方框投影双层分离根修 / 相遇纪念卡低饱和「月光水银」重制 / MCP 浏览器版独立与边界整治） -->\n<!-- v161-p · 心潮视界驾驶舱：记忆视界升级为心潮念综合驾驶舱（情绪驱力图谱 + 梦境时序流 + OB 记忆接管）；Chat 侧栏「视界·心潮驾驶舱」无缝跳转-原位返回；OB 开启时记忆写入/读取全面 OB Only（本地记忆库下线） -->",
    'R9-HEADER')

io.open(P,'w',encoding='utf-8').write(src)
print('ALL DONE, size=', len(src))