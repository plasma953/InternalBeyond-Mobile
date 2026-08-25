# -*- coding: utf-8 -*-
"""v161-p 更名：心潮驾驶舱 → 心潮•念（用户可见文本 + 注释统一）"""
import io
P = '/tmp/ibrepo/index.html'
src = io.open(P, encoding='utf-8').read()

def rep(old, new, tag):
    global src
    c = src.count(old)
    assert c == 1, 'ANCHOR[%s] count=%d' % (tag, c)
    src = src.replace(old, new, 1)
    print('OK R[%s]' % tag)

# ── 文件头注释 ──
rep('心潮视界驾驶舱：记忆视界升级为心潮念综合驾驶舱（情绪驱力图谱 + 梦境时序流 + OB 记忆接管）；Chat 侧栏「视界·心潮驾驶舱」无缝跳转-原位返回',
    '心潮•念：记忆视界升级为心潮念综合视界（情绪驱力图谱 + 梦境时序流 + OB 记忆接管）；Chat 侧栏「心潮•念」无缝跳转-原位返回',
    'H1')
# ── R6 注释与侧栏入口 UI ──
rep('心潮视界驾驶舱——无缝跳转 / 原位返回（全局钩子）', '心潮•念——无缝跳转 / 原位返回（全局钩子）', 'H2')
rep("Chat 侧栏注入「视界 · 心潮驾驶舱」入口", "Chat 侧栏注入「心潮•念」入口", 'H3')
rep('视界 · 心潮驾驶舱</b>', '心潮•念</b>', 'UI-CS')
# ── R2 桥注释 ──
rep('跨模块桥——视界驾驶舱复用快照渲染', '跨模块桥——心潮•念复用快照渲染', 'H4')
# ── R5 尾调用注释 ──
rep('心潮驾驶舱随视界刷新', '心潮•念随视界刷新', 'H5')
# ── R7 驾驶舱实现注释与 UI ──
rep('心潮视界驾驶舱——感知心潮念实时心智（驱力/梦境）+ OB 记忆接管', '心潮•念——感知心潮念实时心智（驱力/梦境）+ OB 记忆接管', 'H6')
rep('注入驾驶舱 DOM（幂等）', '注入心潮•念卡片 DOM（幂等）', 'H7')
rep('>心潮驾驶舱<span', '>心潮•念<span', 'UI-TITLE')
rep('驾驶舱装载中…', '心潮•念装载中…', 'UI-LOADING')
rep('驾驶舱渲染——随视界刷新', '心潮•念渲染——随视界刷新', 'H8')

io.open(P, 'w', encoding='utf-8').write(src)
print('ALL DONE, size =', len(src), ', remaining 驾驶舱 =', src.count('驾驶舱'))