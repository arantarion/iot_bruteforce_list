!function(){"use strict";const t=document.querySelector(".wp-block-msxcm-summary");(()=>{if(!t)return;const e=t.querySelector(".js-expand-summary"),n=t.querySelector("span");if(!e||!n)return;const i=n.innerHTML.trim(),s=i.replace(/\s+/g," ").split(/(?=\s)/gi).slice(0,28).join(""),r=e.getAttribute("data-i18n-more"),a=e.getAttribute("data-i18n-less");function c(i,s){t.classList.toggle("is-expanded");const c=t.classList.contains("is-expanded");e.setAttribute("aria-expanded",c.toString()),n.innerHTML=c?i:s+"...",e.innerHTML=c?a:r,e.dataset.biBhvr=c?8:7}i.length!==s.length&&(c(i,s),e.setAttribute("aria-hidden","false"),e.addEventListener("click",(()=>{c(i,s)})))})()}();