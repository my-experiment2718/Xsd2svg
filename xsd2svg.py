import sys
import xml.etree.ElementTree as ET

SVG_HEADER = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns:ns0="metadata" xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink" baseProfile="full" height="7890" onload="prepareSVG()" version="1.1" width="1702.3">
<style>* {
	user-select: none;
}
.se {
	cursor: pointer;
}
.el {
	cursor: pointer;
}
.at {
	cursor: pointer;
}
.se circle {
	fill: black;
}
.se ellipse:hover{
	fill: #e6e6e6;
}
.co ellipse {
	fill: black;
}
.co line{
	stroke: white;
}
.co circle {
	fill: white;
}
.any {
	fill: #e6e6e6;
}
.hd {
	visibility: hidden;
}
line, ellipse, rectangle, circle, g {
	fill: white;
	stroke: black;
}
text {
	fill: black;
	stroke: none;
	font-family: 'Source Code Pro', monospace;
}
.hi rect {
	fill: #fac832;
	stroke: black;
}
.hi text {
	stroke: none;
}
.el.op {
	stroke: #666;	
}
.el.op text {
	fill: #666;
}
.el.ma {
	stroke: #1e32fa;
}
.el.ma text {
	fill: #1e32fa;
}
.at {
	stroke: #5a14a0;
}
.at text {
	fill: #5a14a0;
}
.el.ke {
	stroke: #289632;
}
.el.ke text {
	fill: #289632;
}
.el.kr {
	stroke: #f050c8;
}
.el.kr text {
	fill: #f050c8;
}
.el.red, .at.red {
	fill: #f0463250;
}</style>
  <script type="text/ecmascript">
function prepareSVG() {
	var root = document.getElementById('_0');
	document.getElementById('_0_0a').onclick = expandAll;
	document.getElementById('_0_0_0b').onclick = collapseAll;
}


function expandAll() {
	var indexes = [0, 0];
	var id;
	var y = delta_y;
	var ymins = [y];
	var ymaxs = [y];
	var el;
	while (true) {
		id = '_' + indexes.join('_');
		if (!ids.includes(id)) {
			indexes.splice(-1, 1);
			ymin = ymins.splice(-1, 1);
			ymax = ymaxs.splice(-1, 1);
			if (indexes.length == 1) {
				break;
			}
			id = '_' + indexes.join('_');

			el = document.getElementById(id+'_0d');
			if (el != null) {
				adjustY_verticalLine(el, ymin, ymax);
			}

			indexes[indexes.length-1] += 1;
			id = '_' + indexes.join('_');
			if (ids.includes(id)) {
				y += delta_y;
				ymaxs[ymaxs.length-1] = y;
			}
		} else {
			el = document.getElementById(id);
			removeAllHidden(el);
			adjustY(el, y);
			for (var letter of "abcdef".split('')) {
				el = document.getElementById(id + letter);
				if (el != null) {
					removeAllHidden(el);
					adjustY(el, y);
				}
			}
			el = document.getElementById(id);
			if (el.classList.contains('co')) {
				el.classList.remove('co');
				el.classList.add('ex');
			}
			indexes = indexes.concat(0);
			ymins = ymins.concat(y);
			ymaxs = ymaxs.concat(y);
		}
	}
}


function collapseAll() {
	var indexes = [0, 0];
	var y = delta_y;
	var ymins = [y, y];
	var id;
	var el;
	var el_d;
	var numberHidden = 0;
	while (true) {
		id = '_' + indexes.join('_');
		if (!ids.includes(id)) {
			indexes.splice(-1, 1);
			ymin = ymins.splice(-1, 1)[0];
			if (indexes.length == 1) {
				break;
			}
			id = '_' + indexes.join('_');
			el_d = document.getElementById(id+'_0d');
			if (el_d != null) {
				y -= delta_y;
			} else if (ids.includes(id+'_0') &amp;&amp; !ids.includes(id+'_1')) {
				y -= delta_y;
			}
			if (el_d != null) {
				adjustY_verticalLine(el_d, ymin, y);
			}
			el = document.getElementById(id);
			
			if (el.classList.contains('se')) {
				numberHidden--;
				y = ymin;
			}
			indexes[indexes.length-1] += 1;
			y += delta_y;
		} else {
			el = document.getElementById(id);
			adjustHidden(el, numberHidden);
			adjustY(el, y);
			for (var letter of "abcdef".split('')) {
				el = document.getElementById(id + letter);
				if (el != null) {
					adjustHidden(el, numberHidden);
					adjustY(el, y);
				}
			}
			el = document.getElementById(id);
			if (el.classList.contains('ex')) {
				el.classList.remove('ex');
				el.classList.add('co');
			}
			if (el.classList.contains('se')) {
				numberHidden++;
			}
			indexes = indexes.concat(0);
			ymins = ymins.concat(y);
		}
	}
}


function removeAllHidden(el) {
	if (el.classList.contains('hd')) {
		el.classList.remove('hd');
		var i = 1;
		while (el.classList.contains('hd'+i)) {
			el.classList.remove('hd'+i);
			i++;
		}
	}
}


function adjustHidden(el, numberHidden) {
	var alreadyHidden = 0;
	if (el.classList.contains('hd')) {
		alreadyHidden = 1;
		while (el.classList.contains('hd'+alreadyHidden)) {
			alreadyHidden++;
		}
	}
	for (var i=alreadyHidden; i&lt;numberHidden; i++) {
		addHidden(el);
	}
}


function adjustY(el, y) {
	// elements and horizontal lines
	if (el.tagName === 'line') {
		el.setAttribute('y1', y);
		el.setAttribute('y2', y);
	} else {
		el.transform.baseVal[0].matrix.f = y;
	}
}


function adjustY_verticalLine(el, ymin, ymax) {
	el.setAttribute('y1', ymin);
	el.setAttribute('y2', ymax);
}


function addHidden(el) {
	if (!el.classList.contains('hd')) {
		el.classList.add('hd');
	} else {
		var i = 1;
		while (el.classList.contains('hd'+i)) {
			i++;
		}
		el.classList.add('hd'+i);
	}
}


function removeHidden(el) {
	if (!el.classList.contains('hd1')) {
		el.classList.remove('hd');
	} else {
		var i = 1;
		while (el.classList.contains('hd'+i)) {
			i++;
		}
		el.classList.remove('hd'+(i-1));
	}
}


function t(sel) {
	/* toggle */
	hiding = sel.classList.contains('ex');
	sel.classList.toggle('ex');
	sel.classList.toggle('co');

	y_start = sel.transform.baseVal[0].matrix.f;
	y_end = y_start
	
	var sel_id = sel.getAttribute('id')
	var id;
	var el;
	var indexes = [0]
	while (true) {
		id = sel_id + '_' + indexes.join('_');
		if (!ids.includes(id)) {
			indexes.splice(-1, 1);
			if (indexes.length == 0) {
				break;
			}
			indexes[indexes.length-1] += 1;
		} else {
			el = document.getElementById(id);
			if (hiding) {
				if (!el.classList.contains('hd')) {
					y_end = Math.max(y_end, el.transform.baseVal[0].matrix.f);
				}
				addHidden(el);
				for (letter of 'abcdef'.split('')) {
					el = document.getElementById(id+letter);
					if (el != null) {
						addHidden(el);
					}
				}
			} else {
				removeHidden(el);
				if (!el.classList.contains('hd')) {
					y_end = Math.max(y_end, el.transform.baseVal[0].matrix.f);
				}
				for (letter of 'abcdef'.split('')) {
					el = document.getElementById(id+letter);
					if (el != null) {
						removeHidden(el);
					}
				}
			}
			indexes = indexes.concat(0);
		}
	}
	
	dy = y_start - y_end;
	if (!hiding) {
		dy = -dy;
	}
	indexes = sel_id.split('_').map(Number);
	indexes.splice(0, 1);
	var root_indexes = indexes.slice();
	var root_id = '';
	
	indexes[indexes.length-1] += 1;
	id = '_' + indexes.join('_');
	if (!ids.includes(id)) {
		indexes.splice(-1, 1);
		if (indexes.length == 0) {
			return;
		}
		indexes[indexes.length-1] += 1;
	}
	while (indexes.length &gt; 1) {
		id = '_' + indexes.join('_');
		if (!ids.includes(id)) {
			indexes.splice(-1, 1);
			id = '_' + indexes.join('_');
			root_id = '_' + root_indexes.slice(0, indexes.length).join('_');
			if (root_id === id &amp;&amp; ids.includes(root_id+'_'+(root_indexes[indexes.length]+1))) {
				el = document.getElementById(id+'_0d');
				if (el != null) {
					el.setAttribute('y2', parseFloat(el.getAttribute('y2')) + dy);
				}
			}
			indexes[indexes.length-1] += 1;
		} else {
			translate(document.getElementById(id), dy);			
			for (var letter of 'abcdef'.split('')) {
				el = document.getElementById(id+letter);
				if (el != null) {
					translate(el, dy);
				}
			}
			indexes = indexes.concat(0);
		}
	}
}


function td(sel) {
	/* toggleDescendants */
	window.event.preventDefault();
	var expand_all_descendants = false;
	if (sel.classList.contains("co")) {
		sel.onclick();
		expand_all_descendants = true;
	}
	var sel_id = sel.getAttribute('id')
	var indexes = [0];
	var id;
	var el;
	while (true) {
		id = sel_id + '_' + indexes.join('_');
		if (!ids.includes(id)) {
			indexes.splice(-1, 1);
			if (indexes.length == 0) {
				break;
			}
			indexes[indexes.length-1] += 1;
		} else {
			el = document.getElementById(id);
			if (el.classList.contains('se')) {
				if (expand_all_descendants) {
					if (el.classList.contains('co')) {
						el.onclick();
					}
				} else {
					el.onclick();
				}
				indexes[indexes.length-1] += 1;
				id = sel_id + '_' + indexes.join('_');
				if (ids.includes(id)) {
					continue;
				}
				indexes.splice(-1, 1);
				if (indexes.length == 0) {
					break;
				}
				indexes[indexes.length-1] += 1;
			} else {
				indexes = indexes.concat(0);
			}
		}
	}
	return false;
}


function translate(el, dy) {
	if (el.tagName === 'line') {
		el.setAttribute('y1', parseFloat(el.getAttribute('y1')) + dy);
		el.setAttribute('y2', parseFloat(el.getAttribute('y2')) + dy);
	} else {
		el.transform.baseVal[0].matrix.f += dy;
	}
}
const ids=["_0","_0_0","_0_0_0","_0_0_0_0","_0_0_0_0_0","_0_0_0_0_0_0","_0_0_0_0_0_0_0","_0_0_0_0_0_0_0_0","_0_0_0_0_0_0_0_0_0","_0_0_0_0_0_0_0_0_1","_0_0_0_0_0_0_0_0_2","_0_0_0_0_0_0_0_0_2_0","_0_0_0_0_0_0_0_0_2_0_0","_0_0_0_0_0_0_0_0_3","_0_0_0_0_0_0_0_0_3_0","_0_0_0_0_0_0_0_0_3_0_0","_0_0_0_0_0_0_0_0_3_0_0_0","_0_0_0_0_0_0_0_0_3_0_0_0_0","_0_0_0_0_0_0_0_0_3_0_1","_0_0_0_0_0_0_0_0_3_0_2","_0_0_0_0_0_0_0_0_3_0_3","_0_0_0_0_0_0_0_0_4","_0_0_0_0_0_0_0_0_4_0","_0_0_0_0_0_0_0_0_4_0_0","_0_0_0_0_0_0_0_0_5","_0_0_0_0_0_0_0_0_5_0","_0_0_0_0_0_0_0_0_5_0_0","_0_0_0_0_0_0_0_0_5_0_0_0","_0_0_0_0_0_0_0_0_5_0_0_0_0","_0_0_0_0_0_0_0_0_5_0_1","_0_0_0_0_0_0_0_0_5_0_2","_0_0_0_0_0_0_0_0_5_0_3","_0_0_0_0_0_0_0_0_6","_0_0_0_0_0_0_0_0_7","_0_0_0_0_0_0_0_0_8","_0_0_0_0_0_0_1","_0_0_0_0_0_0_1_0","_0_0_0_0_0_0_1_0_0","_0_0_0_0_0_0_1_0_0_0","_0_0_0_0_0_0_1_0_1","_0_0_0_0_0_0_1_0_1_0","_0_0_0_0_0_0_1_0_2","_0_0_0_0_0_0_1_0_2_0","_0_0_0_0_0_0_2","_0_0_0_0_0_0_2_0","_0_0_0_0_0_0_2_0_0","_0_0_0_0_0_0_2_0_1","_0_0_0_0_0_0_2_0_1_0","_0_0_0_0_0_0_2_0_1_0_0","_0_0_0_0_0_0_2_0_1_0_0_0","_0_0_0_0_0_0_2_0_1_0_0_0_0","_0_0_0_0_0_0_2_0_1_0_0_0_0_0","_0_0_0_0_0_0_2_0_1_0_0_0_0_0_0","_0_0_0_0_0_0_2_0_1_0_0_0_0_0_1","_0_0_0_0_0_0_2_0_1_0_0_0_1","_0_0_0_0_0_0_2_0_1_0_1","_0_0_0_0_0_0_2_0_1_0_1_0","_0_0_0_0_0_0_2_0_1_0_1_0_0","_0_0_0_0_0_0_2_0_1_0_1_0_0_0","_0_0_0_0_0_0_2_0_1_0_1_0_0_0_0","_0_0_0_0_0_0_2_0_1_0_1_0_0_0_1","_0_0_0_0_0_0_2_0_1_0_1_0_1","_0_0_0_0_0_0_2_0_1_0_1_0_1_0","_0_0_0_0_0_0_2_0_1_0_1_0_1_0_0","_0_0_0_0_0_0_2_0_1_0_1_0_1_0_1","_0_0_0_0_0_0_2_0_1_0_1_0_1_0_2","_0_0_0_0_0_0_2_0_1_0_1_0_2","_0_0_0_0_0_0_2_0_2","_0_0_0_0_0_0_2_0_3","_0_0_0_0_0_0_3","_0_0_0_0_0_0_3_0","_0_0_0_0_0_0_3_0_0","_0_0_0_0_0_0_3_0_1","_0_0_0_0_0_0_3_0_2","_0_0_0_0_0_0_3_0_3","_0_0_0_0_0_0_3_0_4","_0_0_0_0_0_0_3_0_5","_0_0_0_0_0_0_3_0_6","_0_0_0_0_0_0_3_0_6_0","_0_0_0_0_0_0_3_0_7","_0_0_0_0_0_0_3_0_7_0","_0_0_0_0_1","_0_0_0_0_1_0","_0_0_0_0_1_0_0","_0_0_0_0_1_0_0_0","_0_0_0_0_1_0_0_0_0","_0_0_0_0_1_0_0_0_0_0","_0_0_0_0_1_0_0_0_0_0_0","_0_0_0_0_1_0_0_0_1","_0_0_0_0_1_0_0_0_2","_0_0_0_0_1_0_0_0_3","_0_0_0_0_1_0_1","_0_0_0_0_1_0_1_0","_0_0_0_0_1_0_1_0_0","_0_0_0_0_1_0_1_0_1","_0_0_0_0_1_0_1_0_2","_0_0_0_0_1_0_1_0_2_0","_0_0_0_0_1_0_1_0_2_0_0","_0_0_0_0_1_0_1_0_2_0_0_0","_0_0_0_0_1_0_1_0_2_0_0_0_0","_0_0_0_0_1_0_1_0_2_0_1","_0_0_0_0_1_0_1_0_2_0_2","_0_0_0_0_1_0_1_0_2_0_2_0","_0_0_0_0_1_0_1_0_2_0_2_0_0","_0_0_0_0_1_0_1_0_2_0_2_0_1","_0_0_0_0_1_0_1_0_2_0_2_0_2","_0_0_0_0_1_0_1_0_2_0_3","_0_0_0_0_1_0_1_0_2_0_4","_0_0_0_0_1_0_1_0_2_0_4_0","_0_0_0_0_1_0_1_0_2_0_4_0_0","_0_0_0_0_1_0_1_0_2_0_4_0_1","_0_0_0_0_1_0_1_0_2_0_4_0_1_0","_0_0_0_0_1_0_1_0_2_0_4_0_1_0_0","_0_0_0_0_1_0_1_0_2_0_4_0_2","_0_0_0_0_1_0_1_0_2_0_4_0_3","_0_0_0_0_1_0_1_0_2_0_4_0_4","_0_0_0_0_1_0_1_0_2_0_4_0_5","_0_0_0_0_1_0_1_0_2_0_5","_0_0_0_0_1_0_1_0_2_0_5_0","_0_0_0_0_1_0_1_0_2_0_5_0_0","_0_0_0_0_1_0_1_0_3","_0_0_0_0_1_0_1_0_3_0","_0_0_0_0_1_0_1_0_3_0_0","_0_0_0_0_1_0_2","_0_0_0_0_1_0_3","_0_0_0_0_1_0_4","_0_0_0_0_1_0_5","_0_0_0_0_2","_0_0_0_0_2_0","_0_0_0_0_2_0_0","_0_0_0_0_2_0_1","_0_0_0_0_2_0_2","_0_0_0_0_2_0_2_0","_0_0_0_0_2_0_2_1","_0_0_0_0_2_0_2_2","_0_0_0_0_2_0_2_3","_0_0_0_0_2_0_2_4","_0_0_0_0_2_0_2_5","_0_0_0_0_2_0_2_6","_0_0_0_0_2_0_2_7","_0_0_0_0_2_0_2_8","_0_0_0_0_2_0_3","_0_0_0_0_2_0_4","_0_0_0_0_2_0_5","_0_0_0_0_2_0_5_0","_0_0_0_0_2_0_5_1","_0_0_0_0_2_0_5_2","_0_0_0_0_2_0_5_3","_0_0_0_0_2_0_5_4","_0_0_0_0_2_0_5_5","_0_0_0_0_2_0_5_6","_0_0_0_0_2_0_5_7","_0_0_0_0_2_0_5_8","_0_0_0_0_2_0_6","_0_0_0_0_2_0_7","_0_0_0_0_2_0_8","_0_0_0_0_3","_0_0_0_0_3_0","_0_0_0_0_3_1","_0_0_0_0_3_2","_0_0_0_0_3_3","_0_0_0_0_3_4","_0_0_0_0_3_5","_0_0_0_0_3_6","_0_0_0_0_3_7","_0_0_0_0_3_8","_0_0_0_0_4","_0_0_0_0_5","_0_0_0_0_5_0","_0_0_0_0_5_0_0","_0_0_0_0_5_0_1","_0_0_0_0_5_0_1_0","_0_0_0_0_5_0_1_0_0","_0_0_0_0_5_0_1_0_0_0","_0_0_0_0_5_0_1_0_0_0_0","_0_0_0_0_5_0_1_0_1","_0_0_0_0_5_0_1_0_2","_0_0_0_0_5_0_1_0_2_0","_0_0_0_0_5_0_1_0_2_0_0","_0_0_0_0_5_0_1_0_2_0_1","_0_0_0_0_5_0_1_0_2_0_2","_0_0_0_0_5_0_1_0_3","_0_0_0_0_5_0_1_0_4","_0_0_0_0_5_0_1_0_4_0","_0_0_0_0_5_0_1_0_4_0_0","_0_0_0_0_5_0_1_0_4_0_1","_0_0_0_0_5_0_1_0_4_0_1_0","_0_0_0_0_5_0_1_0_4_0_1_0_0","_0_0_0_0_5_0_1_0_4_0_2","_0_0_0_0_5_0_1_0_4_0_3","_0_0_0_0_5_0_1_0_4_0_4","_0_0_0_0_5_0_1_0_4_0_5","_0_0_0_0_5_0_1_0_5","_0_0_0_0_5_0_1_0_5_0","_0_0_0_0_5_0_1_0_5_0_0","_0_0_0_0_5_0_2","_0_0_0_0_5_0_3","_0_0_0_0_5_0_3_0","_0_0_0_0_5_0_3_0_0","_0_0_0_0_5_0_3_0_1","_0_0_0_0_6","_0_0_0_0_6_0","_0_0_0_0_6_0_0","_0_0_0_0_6_0_1","_0_0_0_0_6_0_2","_0_0_0_0_6_0_2_0","_0_0_0_0_6_0_2_1","_0_0_0_0_6_0_2_2","_0_0_0_0_6_0_2_3","_0_0_0_0_6_0_2_4","_0_0_0_0_6_0_2_5","_0_0_0_0_6_0_2_6","_0_0_0_0_6_0_2_7","_0_0_0_0_6_0_2_8","_0_0_0_0_6_0_3","_0_0_0_0_6_0_4","_0_0_0_0_6_0_5","_0_0_0_0_6_0_6","_0_0_0_0_6_0_7","_0_0_0_0_6_0_7_0","_0_0_0_0_6_0_7_1","_0_0_0_0_6_0_7_2","_0_0_0_0_6_0_7_3","_0_0_0_0_6_0_7_4","_0_0_0_0_6_0_7_5","_0_0_0_0_6_0_7_6","_0_0_0_0_6_0_7_7","_0_0_0_0_6_0_7_8","_0_0_0_0_6_0_8","_0_0_0_0_6_0_9","_0_0_0_0_6_0_10","_0_0_0_0_7","_0_0_0_0_7_0","_0_0_0_0_7_0_0","_0_0_0_0_7_0_1","_0_0_0_0_7_0_1_0","_0_0_0_0_7_0_1_0_0","_0_0_0_0_7_0_1_0_0_0","_0_0_0_0_7_0_1_0_0_0_0","_0_0_0_0_7_0_1_0_1","_0_0_0_0_7_0_1_0_2","_0_0_0_0_7_0_1_0_2_0","_0_0_0_0_7_0_1_0_2_0_0","_0_0_0_0_7_0_1_0_2_0_1","_0_0_0_0_7_0_1_0_2_0_2","_0_0_0_0_7_0_1_0_3","_0_0_0_0_7_0_1_0_4","_0_0_0_0_7_0_1_0_4_0","_0_0_0_0_7_0_1_0_4_0_0","_0_0_0_0_7_0_1_0_4_0_1","_0_0_0_0_7_0_1_0_4_0_1_0","_0_0_0_0_7_0_1_0_4_0_1_0_0","_0_0_0_0_7_0_1_0_4_0_2","_0_0_0_0_7_0_1_0_4_0_3","_0_0_0_0_7_0_1_0_4_0_4","_0_0_0_0_7_0_1_0_4_0_5","_0_0_0_0_7_0_1_0_5","_0_0_0_0_7_0_1_0_5_0","_0_0_0_0_7_0_1_0_5_0_0","_0_0_0_0_7_0_2","_0_0_0_0_7_0_3","_0_0_0_0_7_0_3_0","_0_0_0_0_7_0_3_0_0","_0_0_0_0_7_0_3_0_1","_0_0_0_0_8","_0_0_0_0_8_0","_0_0_0_0_8_0_0","_0_0_0_0_9","_0_0_0_0_10","_0_0_0_0_10_0","_0_0_0_0_10_0_0","_0_0_0_0_10_0_1","_0_0_0_0_11","_0_0_0_0_11_0","_0_0_0_0_11_0_0","_0_0_0_0_11_0_1","_0_0_0_0_11_0_2","_0_0_0_0_11_0_2_0","_0_0_0_0_11_0_2_1","_0_0_0_0_11_0_2_2","_0_0_0_0_11_0_2_3","_0_0_0_0_11_0_2_4","_0_0_0_0_11_0_2_5","_0_0_0_0_11_0_2_6","_0_0_0_0_11_0_2_7","_0_0_0_0_11_0_2_8","_0_0_0_0_11_0_3","_0_0_0_0_11_0_4","_0_0_0_0_11_0_5","_0_0_0_0_11_0_6","_0_0_0_0_11_0_6_0","_0_0_0_0_11_0_6_1","_0_0_0_0_11_0_6_2","_0_0_0_0_11_0_6_3","_0_0_0_0_11_0_6_4","_0_0_0_0_11_0_6_5","_0_0_0_0_11_0_6_6","_0_0_0_0_11_0_6_7","_0_0_0_0_11_0_6_8","_0_0_0_0_11_0_7","_0_0_0_0_11_0_8","_0_0_0_0_11_0_9","_0_0_0_0_11_0_10","_0_0_0_0_12","_0_0_0_0_12_0","_0_0_0_0_12_0_0","_0_0_0_0_12_0_0_0","_0_0_0_0_12_0_0_0_0","_0_0_0_0_12_0_0_0_1","_0_0_0_0_12_0_0_0_2","_0_0_0_0_12_0_1","_0_0_0_0_12_0_2","_0_0_0_0_12_0_2_0","_0_0_0_0_12_0_2_0_0","_0_0_0_0_12_0_2_0_1","_0_0_0_0_12_0_2_0_1_0","_0_0_0_0_12_0_2_0_1_0_0","_0_0_0_0_12_0_2_0_1_0_0_0","_0_0_0_0_12_0_2_0_1_0_0_0_0","_0_0_0_0_12_0_2_0_1_0_1","_0_0_0_0_12_0_2_0_1_0_2","_0_0_0_0_12_0_2_0_1_0_2_0","_0_0_0_0_12_0_2_0_1_0_2_0_0","_0_0_0_0_12_0_2_0_1_0_2_0_1","_0_0_0_0_12_0_2_0_1_0_2_0_2","_0_0_0_0_12_0_2_0_1_0_3","_0_0_0_0_12_0_2_0_1_0_4","_0_0_0_0_12_0_2_0_1_0_4_0","_0_0_0_0_12_0_2_0_1_0_4_0_0","_0_0_0_0_12_0_2_0_1_0_4_0_1","_0_0_0_0_12_0_2_0_1_0_4_0_1_0","_0_0_0_0_12_0_2_0_1_0_4_0_1_0_0","_0_0_0_0_12_0_2_0_1_0_4_0_2","_0_0_0_0_12_0_2_0_1_0_4_0_3","_0_0_0_0_12_0_2_0_1_0_4_0_4","_0_0_0_0_12_0_2_0_1_0_4_0_5","_0_0_0_0_12_0_2_0_1_0_5","_0_0_0_0_12_0_2_0_1_0_5_0","_0_0_0_0_12_0_2_0_1_0_5_0_0","_0_0_0_0_12_0_2_0_2","_0_0_0_0_12_0_2_0_3","_0_0_0_0_12_0_2_0_3_0","_0_0_0_0_12_0_2_0_3_0_0","_0_0_0_0_12_0_2_0_3_0_1","_0_0_0_0_12_0_3","_0_0_0_0_12_0_3_0","_0_0_0_0_12_0_3_0_0","_0_0_0_0_12_0_3_0_1","_0_0_0_0_12_0_3_0_1_0","_0_0_0_0_12_0_3_0_1_0_0","_0_0_0_0_12_0_3_0_1_0_0_0","_0_0_0_0_12_0_3_0_1_0_0_0_0","_0_0_0_0_12_0_3_0_1_0_1","_0_0_0_0_12_0_3_0_1_0_2","_0_0_0_0_12_0_3_0_1_0_2_0","_0_0_0_0_12_0_3_0_1_0_2_0_0","_0_0_0_0_12_0_3_0_1_0_2_0_1","_0_0_0_0_12_0_3_0_1_0_2_0_2","_0_0_0_0_12_0_3_0_1_0_3","_0_0_0_0_12_0_3_0_1_0_4","_0_0_0_0_12_0_3_0_1_0_4_0","_0_0_0_0_12_0_3_0_1_0_4_0_0","_0_0_0_0_12_0_3_0_1_0_4_0_1","_0_0_0_0_12_0_3_0_1_0_4_0_1_0","_0_0_0_0_12_0_3_0_1_0_4_0_1_0_0","_0_0_0_0_12_0_3_0_1_0_4_0_2","_0_0_0_0_12_0_3_0_1_0_4_0_3","_0_0_0_0_12_0_3_0_1_0_4_0_4","_0_0_0_0_12_0_3_0_1_0_4_0_5","_0_0_0_0_12_0_3_0_1_0_5","_0_0_0_0_12_0_3_0_1_0_5_0","_0_0_0_0_12_0_3_0_1_0_5_0_0","_0_0_0_0_12_0_3_0_2","_0_0_0_0_12_0_3_0_3","_0_0_0_0_12_0_3_0_3_0","_0_0_0_0_12_0_3_0_3_0_0","_0_0_0_0_12_0_3_0_3_0_1","_0_0_0_0_12_0_4","_0_0_0_0_12_0_4_0","_0_0_0_0_12_0_4_0_0","_0_0_0_0_12_0_4_0_1","_0_0_0_0_12_0_5","_0_0_0_0_12_0_6","_0_0_0_0_12_0_7","_0_0_0_0_12_0_7_0","_0_0_0_0_12_0_7_0_0","_0_0_0_0_12_0_7_0_0_0","_0_0_0_0_12_0_7_0_0_0_0","_0_0_0_0_12_0_7_0_0_0_0_0","_0_0_0_0_12_0_7_0_0_0_0_0_0","_0_0_0_0_12_0_7_0_0_0_0_0_1","_0_0_0_0_12_0_7_0_0_0_0_0_1_0","_0_0_0_0_12_0_7_0_0_0_0_0_1_0_0","_0_0_0_0_12_0_7_0_0_0_1","_0_0_0_0_12_0_7_0_0_0_2","_0_0_0_0_12_0_7_0_1","_0_0_0_0_12_0_7_0_1_0","_0_0_0_0_12_0_7_0_1_0_0","_0_0_0_0_12_0_7_0_1_0_1","_0_0_0_0_12_0_7_0_1_0_2","_0_0_0_0_12_0_7_0_1_0_2_0","_0_0_0_0_12_0_7_0_1_0_2_0_0","_0_0_0_0_12_0_7_0_1_0_2_0_1","_0_0_0_0_12_0_7_0_1_0_2_0_2","_0_0_0_0_12_0_8","_0_0_0_0_12_0_8_0","_0_0_0_0_12_0_8_0_0","_0_0_0_0_12_0_8_0_1","_0_0_0_0_12_0_8_0_2","_0_0_0_0_12_0_8_0_3","_0_0_0_0_12_0_8_0_4","_0_0_0_0_12_0_8_0_5","_0_0_0_0_12_0_8_0_5_0","_0_0_0_0_12_0_8_0_5_0_0","_0_0_0_0_12_0_8_0_5_0_1","_0_0_0_0_12_0_8_0_6","_0_0_0_0_13","_0_0_0_0_14","_0_0_0_0_14_0","_0_0_0_0_14_0_0","_0_0_0_0_14_0_1","_0_0_0_0_14_0_2","_0_0_0_0_14_0_3","_0_0_0_0_14_0_4","_0_0_0_0_14_0_5","_0_0_0_0_14_0_5_0","_0_0_0_0_14_0_5_0_0","_0_0_0_0_14_0_5_0_1","_0_0_0_0_14_0_5_0_2","_0_0_0_0_14_0_5_0_3","_0_0_0_0_14_0_5_0_4","_0_0_0_0_14_0_6","_0_0_1"];const delta_x = 22; const delta_y = 30;</script>
  <defs/>

'''
SVG_FOOTER = '</svg>'

# Color palette for elements
COLORS = ["#8ecae6", "#219ebc", "#023047", "#ffb703", "#fb8500"]

def parse_xsd_tree(elem, ns, types, depth=0):
    """
    Recursively parse XSD elements and complex types into a tree structure.
    Returns a list of dicts: {name, type, children, depth, minOccurs, maxOccurs, attributes}
    """
    nodes = []
    for child in elem.findall('xs:element', ns):
        doc = ''
        ann = child.find('xs:annotation/xs:documentation', ns)
        if ann is not None and ann.text:
            doc = ann.text.strip()
        name = child.attrib.get('name', '')
        type_ = child.attrib.get('type', '')
        minOccurs = child.attrib.get('minOccurs', '1')
        maxOccurs = child.attrib.get('maxOccurs', '1')
        # Parse attributes if any
        attributes = []
        ct = None
        children = []
        # Always expand referenced types recursively
        if not type_:
            ct = child.find('xs:complexType', ns)
        elif type_ in types:
            ct = types[type_]
        if ct is not None:
            # Attributes
            for attr in ct.findall('xs:attribute', ns):
                attr_name = attr.attrib.get('name', '')
                attr_type = attr.attrib.get('type', '')
                attr_use = attr.attrib.get('use', 'optional')
                attr_doc = ''
                attr_ann = attr.find('xs:annotation/xs:documentation', ns)
                if attr_ann is not None and attr_ann.text:
                    attr_doc = attr_ann.text.strip()
                attributes.append({'name': attr_name, 'type': attr_type, 'use': attr_use, 'doc': attr_doc})
            seq = ct.find('xs:sequence', ns)
            if seq is not None:
                children = parse_xsd_tree(seq, ns, types, depth+1)
        nodes.append({
            'name': name,
            'type': type_,
            'children': children,
            'depth': depth,
            'minOccurs': minOccurs,
            'maxOccurs': maxOccurs,
            'attributes': attributes,
            'doc': doc
        })
    return nodes

def collect_types(root, ns):
    """Collect named complexTypes in the schema."""
    types = {}
    for ct in root.findall('.//xs:complexType', ns):
        name = ct.attrib.get('name')
        if name:
            types[name] = ct
    return types

def parse_xsd(xsd_path):
    tree = ET.parse(xsd_path)
    root = tree.getroot()
    ns = {'xs': 'http://www.w3.org/2001/XMLSchema'}
    types = collect_types(root, ns)
    # Find top-level elements
    elements = []
    for elem in root.findall('xs:element', ns):
        doc = ''
        ann = elem.find('xs:annotation/xs:documentation', ns)
        if ann is not None and ann.text:
            doc = ann.text.strip()
        name = elem.attrib.get('name', '')
        type_ = elem.attrib.get('type', '')
        minOccurs = elem.attrib.get('minOccurs', '1')
        maxOccurs = elem.attrib.get('maxOccurs', '1')
        attributes = []
        children = []
        ct = None
        # Always expand referenced types recursively
        if not type_:
            ct = elem.find('xs:complexType', ns)
        elif type_ in types:
            ct = types[type_]
        if ct is not None:
            # Attributes
            for attr in ct.findall('xs:attribute', ns):
                attr_name = attr.attrib.get('name', '')
                attr_type = attr.attrib.get('type', '')
                attr_use = attr.attrib.get('use', 'optional')
                attr_doc = ''
                attr_ann = attr.find('xs:annotation/xs:documentation', ns)
                if attr_ann is not None and attr_ann.text:
                    attr_doc = attr_ann.text.strip()
                attributes.append({'name': attr_name, 'type': attr_type, 'use': attr_use, 'doc': attr_doc})
            seq = ct.find('xs:sequence', ns)
            if seq is not None:
                children = parse_xsd_tree(seq, ns, types, 1)
        elements.append({
            'name': name,
            'type': type_,
            'children': children,
            'depth': 0,
            'minOccurs': minOccurs,
            'maxOccurs': maxOccurs,
            'attributes': attributes,
            'doc': doc
        })
    return elements
'''
  <line id="_0_0_0b" x1="229.0" x2="251.0" y1="30" y2="30" class="hd"/>
  <line id="_0_0_0c" x1="251.0" x2="273.0" y1="30" y2="30" class="hd"/>
  <g class="el ma hd" id="_0_0_0" transform="matrix(1 0 0 1 273 30)">
    <rect height="19.6" width="86.2" x="0" y="-9.8">
      <title>Active segment of bag journey including relevant details</title>
      <metadata>
        <ns0:xd>
          <ns0:ty>BagSegmentType</ns0:ty>
        </ns0:xd>
      </metadata>
    </rect>
    <text font-family="monospace" font-size="14" x="2.8" y="4.9">BagSegment</text>
  </g>
  <line id="_0_0_0_0a" x1="359.2" x2="381.2" y1="30" y2="30" class="hd"/>
  <g class="se hd co" id="_0_0_0_0" onclick="t(this)" oncontextmenu="td(this)" transform="matrix(1 0 0 1 381.2 30)">
    <ellipse cx="18" cy="0" rx="18" ry="12"/>
    <line x1="4" x2="32" y1="0" y2="0"/>
    <circle cx="10" cy="0" r="2"/>
    <circle cx="18" cy="0" r="2"/>
    <circle cx="26" cy="0" r="2"/>
  </g>
'''

def draw_tree_svg(nodes, svg, x, y, xstep, ystep):
    """Draw nodes as a tree, recursively, with attributes and occurrence info."""
    y_offset = y
    for i, node in enumerate(nodes):
        box_x = x + node['depth'] * xstep
        box_y = y_offset
        width, height = 180, 28
        
        # Determine class and style for optional/mandatory
        min_occ = str(node.get('minOccurs', '1'))
        el_class = 'el ma' if min_occ != '0' else 'el op' #add hd hd1 hd2 for hiding
        #rect_style = ''
        #if min_occ == '0':
        #    rect_style = 'stroke-dasharray:5 5;'
        
        # Group for element with ID
        el_id = f'el_{box_x}_{box_y}'
        # svg.append(f'<g id="{el_id}" transform="translate({box_x},{box_y})">')
        # Draw element box
        # svg.append(f'<rect width="{width}" height="{height}" y="0" x="0" class="{el_class}" style="{rect_style}">')
        # Tooltip: doc, type, min/maxOccurs
        '''tooltip = node.get('doc', '')
        if node.get('type'):
            tooltip += f'\nType: {node["type"]}'
        tooltip += f'\nOccurs: [{node["minOccurs"]},{node["maxOccurs"]}]'
        svg.append(f'<title>{tooltip.strip()}</title>')
        '''
        #svg.append('</rect>')

        # Only show element name in box
        #svg.append(f'<text x="8" y="18" class="eltext">{node["name"]}</text>')
        
        # Draw attributes below the box
        attr_y = height + 4
        for k, attr in enumerate(node['attributes']):
            svg.append(f'<rect x="12" y="{attr_y + k*18}" width="{width-24}" height="16" class="at" >')
            attr_tooltip = attr.get('doc', '')
            if attr.get('type'):
                attr_tooltip += f'\nType: {attr["type"]}'
            attr_tooltip += f'\nUse: {attr["use"]}'
            svg.append(f'<title>{attr_tooltip.strip()}</title>')
            svg.append('</rect>')
            attr_label = f"@{attr['name']}"
            svg.append(f'<text x="18" y="{attr_y + k*18 + 13}" class="attext">{attr_label}</text>')
        svg.append('</g>')
        
        # Draw lines to children
        child_y_start = box_y + height // 2
        for j, child in enumerate(node['children']):
            child_x = box_x + xstep
            child_y = y_offset + j * ystep
            svg.append(f'<line x1="{box_x+width}" y1="{child_y_start}" x2="{child_x}" y2="{child_y+height//2}" class="edge" />')
        
        # Draw children
        draw_tree_svg(node['children'], svg, x + xstep, y_offset, xstep, ystep, color_idx)
        # Update y_offset for next sibling
        y_offset += height + max(len(node['attributes']), 1) * 18 + 8

def elements_to_svg(elements, svg_path):
    svg = [SVG_HEADER]
    x, y = 50, 50
    xstep, ystep = 300, 70
    draw_tree_svg(elements, svg, x, y, xstep, ystep)
    svg.append(SVG_FOOTER)
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))

def main():
    if len(sys.argv) != 3:
        print("Usage: python xsd2svg.py input.xsd output.svg")
        sys.exit(1)
    xsd_path = sys.argv[1]
    svg_path = sys.argv[2]
    elements = parse_xsd(xsd_path)
    elements_to_svg(elements, svg_path)
    print(f"SVG file generated: {svg_path}")

if __name__ == "__main__":
    main()
