// Shared header behaviour: desktop dropdowns, phone burger menu.
(function(){
  var dds=[].slice.call(document.querySelectorAll('.dd'));
  var fine=window.matchMedia&&matchMedia('(hover:hover) and (pointer:fine)').matches;
  function setDd(d,open){d.classList.toggle('open',open);var b=d.querySelector('.dd-btn');if(b)b.setAttribute('aria-expanded',open?'true':'false');}
  function closeAll(except){dds.forEach(function(d){if(d!==except)setDd(d,false);});}
  dds.forEach(function(d){
    var b=d.querySelector('.dd-btn'),t=null;
    b.addEventListener('click',function(e){e.stopPropagation();var o=!d.classList.contains('open');closeAll(d);setDd(d,o);});
    if(fine){
      d.addEventListener('mouseenter',function(){clearTimeout(t);closeAll(d);setDd(d,true);});
      d.addEventListener('mouseleave',function(){t=setTimeout(function(){setDd(d,false);},160);});
    }
    d.addEventListener('focusout',function(e){if(!d.contains(e.relatedTarget))setDd(d,false);});
  });
  document.addEventListener('click',function(e){if(!e.target.closest||!e.target.closest('.dd'))closeAll();});

  var bg=document.querySelector('.burger'),mn=document.getElementById('mnav');
  function setMenu(open){
    if(!bg||!mn)return;
    bg.setAttribute('aria-expanded',open?'true':'false');
    bg.setAttribute('aria-label',open?'Close menu':'Open menu');
    mn.classList.toggle('open',open);mn.setAttribute('aria-hidden',open?'false':'true');
    document.body.classList.toggle('menu-open',open);
    if(open){var h=document.querySelector('.sh');if(h)mn.style.top=h.getBoundingClientRect().bottom+'px';}
  }
  if(bg&&mn){
    bg.addEventListener('click',function(){setMenu(bg.getAttribute('aria-expanded')!=='true');});
    mn.querySelectorAll('.macc').forEach(function(b){b.addEventListener('click',function(){var li=b.parentNode,o=!li.classList.contains('open');li.classList.toggle('open',o);b.setAttribute('aria-expanded',o?'true':'false');});});
    mn.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){setMenu(false);});});
    window.addEventListener('resize',function(){if(innerWidth>900)setMenu(false);});
  }
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeAll();setMenu(false);}});
})();
