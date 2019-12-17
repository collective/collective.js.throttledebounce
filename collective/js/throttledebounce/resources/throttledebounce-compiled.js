/*!
 * jQuery throttle / debounce - v1.1 - 3/7/2010
 * http://benalman.com/projects/jquery-throttle-debounce-plugin/
 *
 * Copyright (c) 2010 "Cowboy" Ben Alman
 * Dual licensed under the MIT and GPL licenses.
 * http://benalman.com/about/license/
 */

// Copyright (c) 2010 "Cowboy" Ben Alman,

// Dual licensed under the MIT and GPL licenses.

// http://benalman.com/about/license/

!function(e,t){"function"==typeof define&&define.amd?define("throttledebounce",["jquery"],t):t(e.jQuery)}("undefined"!=typeof self?self:this,function(e){"$:nomunge";jq_throttle,e.throttle=jq_throttle=function(t,n,o,i){function u(){function e(){f=+new Date,o.apply(r,l)}function u(){d=void 0}var r=this,c=+new Date-f,l=arguments;i&&!d&&e(),d&&clearTimeout(d),void 0===i&&c>t?e():!0!==n&&(d=setTimeout(i?u:e,void 0===i?t-c:t))}var d,f=0;return"boolean"!=typeof n&&(i=o,o=n,n=void 0),e.guid&&(u.guid=o.guid=o.guid||e.guid++),u},e.debounce=function(e,t,n){return void 0===n?jq_throttle(e,t,!1):jq_throttle(e,n,!1!==t)}}),require(["throttledebounce"],function(e){}),define("main",function(){});