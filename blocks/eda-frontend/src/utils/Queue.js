/* eslint-disable */
//code.stephenmorley.org
export function Queue(){let a=[],b=0;this.getLength=function(){return a.length-b};this.isEmpty=function(){return 0===a.length};this.enqueue=function(b){a.push(b)};this.dequeue=function(){if(0!==a.length){const c=a[b];if(2*(++b)>=a.length){a=a.slice(b);b=0};return c}};this.peek=function(){return 0<a.length?a[b]:void 0}};