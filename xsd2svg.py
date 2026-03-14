import sys
import xml.etree.ElementTree as ET

SVG_HEADER = '''<svg xmlns="http://www.w3.org/2000/svg" width="3000" height="3000">
<style>
    .el { fill: #8ecae6; stroke: #333; }
    .at { fill: #ffb703; stroke: #333; }
    .eltext { fill: #023047; font-size: 16px; font-family: 'Source Code Pro', monospace; }
    .attext { fill: #fb8500; font-size: 13px; font-family: 'Source Code Pro', monospace; }
    .edge { stroke: #888; stroke-width: 2; }
</style>
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

def draw_tree_svg(nodes, svg, x, y, xstep, ystep, color_idx=0):
    """Draw nodes as a tree, recursively, with attributes and occurrence info."""
    y_offset = y
    for i, node in enumerate(nodes):
        color = COLORS[(color_idx + node['depth']) % len(COLORS)]
        box_x = x + node['depth'] * xstep
        box_y = y_offset
        width, height = 180, 28
        # Determine class and style for optional/mandatory
        min_occ = str(node.get('minOccurs', '1'))
        el_class = 'el ma' if min_occ != '0' else 'el op'
        rect_style = ''
        if min_occ == '0':
            rect_style = 'stroke-dasharray:5 5;'
        # Group for element with ID
        el_id = f'el_{box_x}_{box_y}'
        svg.append(f'<g id="{el_id}" transform="translate({box_x},{box_y})">')
        # Draw element box
        svg.append(f'<rect width="{width}" height="{height}" y="0" x="0" class="{el_class}" style="{rect_style}">')
        # Tooltip: doc, type, min/maxOccurs
        tooltip = node.get('doc', '')
        if node.get('type'):
            tooltip += f'\nType: {node["type"]}'
        tooltip += f'\nOccurs: [{node["minOccurs"]},{node["maxOccurs"]}]'
        svg.append(f'<title>{tooltip.strip()}</title>')
        svg.append('</rect>')
        # Only show element name in box
        svg.append(f'<text x="8" y="18" class="eltext">{node["name"]}</text>')
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
