#!/usr/bin/env python3
"""Insert images into presentation slides."""

import sys
sys.path.insert(0, '/Users/stevehill/.claude/plugins/marketplaces/anthropic-agent-skills/document-skills/pptx/ooxml')

from lxml import etree
from pathlib import Path

# Namespaces
NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a16': 'http://schemas.microsoft.com/office/drawing/2014/main',
    'p14': 'http://schemas.microsoft.com/office/powerpoint/2010/main'
}

# Register namespaces
for prefix, uri in NS.items():
    etree.register_namespace(prefix, uri)

def add_image_to_slide(slide_path, rels_path, image_rel_id, image_target, x_pos, y_pos, width, height, pic_id, pic_name):
    """Add an image element to a slide."""

    # Read slide XML
    tree = etree.parse(str(slide_path))
    root = tree.getroot()

    # Find spTree
    sp_tree = root.find('.//p:cSld/p:spTree', NS)

    # Create picture element
    pic = etree.Element('{%s}pic' % NS['p'])

    # nvPicPr (non-visual picture properties)
    nv_pic_pr = etree.SubElement(pic, '{%s}nvPicPr' % NS['p'])
    c_nv_pr = etree.SubElement(nv_pic_pr, '{%s}cNvPr' % NS['p'], id=str(pic_id), name=pic_name)
    etree.SubElement(nv_pic_pr, '{%s}cNvPicPr' % NS['p'])
    etree.SubElement(nv_pic_pr, '{%s}nvPr' % NS['p'])

    # blipFill (image fill)
    blip_fill = etree.SubElement(pic, '{%s}blipFill' % NS['p'])
    blip = etree.SubElement(blip_fill, '{%s}blip' % NS['a'])
    blip.set('{%s}embed' % NS['r'], image_rel_id)
    stretch = etree.SubElement(blip_fill, '{%s}stretch' % NS['a'])
    etree.SubElement(stretch, '{%s}fillRect' % NS['a'])

    # spPr (shape properties with position and size)
    sp_pr = etree.SubElement(pic, '{%s}spPr' % NS['p'])
    xfrm = etree.SubElement(sp_pr, '{%s}xfrm' % NS['a'])
    off = etree.SubElement(xfrm, '{%s}off' % NS['a'], x=str(x_pos), y=str(y_pos))
    ext = etree.SubElement(xfrm, '{%s}ext' % NS['a'], cx=str(width), cy=str(height))
    prst_geom = etree.SubElement(sp_pr, '{%s}prstGeom' % NS['a'], prst='rect')
    etree.SubElement(prst_geom, '{%s}avLst' % NS['a'])

    # Insert picture before first shape (after grpSpPr)
    grp_sp_pr = sp_tree.find('p:grpSpPr', NS)
    grp_sp_pr_index = list(sp_tree).index(grp_sp_pr)
    sp_tree.insert(grp_sp_pr_index + 1, pic)

    # Write slide XML
    tree.write(str(slide_path), encoding='ascii', xml_declaration=True, pretty_print=True)

    # Create/update relationships file
    rels_path.parent.mkdir(exist_ok=True)

    if rels_path.exists():
        rels_tree = etree.parse(str(rels_path))
        rels_root = rels_tree.getroot()
    else:
        rels_root = etree.Element('Relationships', xmlns='http://schemas.openxmlformats.org/package/2006/relationships')
        rels_tree = etree.ElementTree(rels_root)
        # Add slideLayout relationship (always rId1)
        etree.SubElement(rels_root, 'Relationship',
            Id='rId1',
            Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout',
            Target='../slideLayouts/slideLayout2.xml')

    # Add image relationship
    etree.SubElement(rels_root, 'Relationship',
        Id=image_rel_id,
        Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/image',
        Target=image_target)

    # Write relationships
    rels_tree.write(str(rels_path), encoding='ascii', xml_declaration=True, pretty_print=True)

    print(f"✓ Added image to {slide_path.name}")

# Slide 10 (slide 9 in user terms) - Systems montage
# Position: Below text, centered
# Montage is 7200x1400 (5:1 ratio)
# EMU units: 914400 per inch
# Slide is 10" x 7.5"
# Image width: 9" = 8229600 EMU
# Image height: 1.75" = 1600200 EMU
# X position: Center = (10" - 9") / 2 = 0.5" = 457200 EMU
# Y position: Below text at 5" = 4572000 EMU

slide10_path = Path('presentation-unpacked/ppt/slides/slide10.xml')
slide10_rels = Path('presentation-unpacked/ppt/slides/_rels/slide10.xml.rels')

add_image_to_slide(
    slide10_path,
    slide10_rels,
    'rId2',
    '../media/image6.jpg',
    457200,    # x: 0.5"
    4572000,   # y: 5"
    8229600,   # width: 9"
    1600200,   # height: 1.75"
    10,        # pic id
    'Systems Montage'
)

# Slide 28 (slide 27 in user terms) - Lesson screenshot
# C64 screenshot is 384x272 (very small)
# Scale up 5x = 1920x1360 pixels at 96 DPI = 20" x 14.17"
# That's too big, use 3x = 1152x816 pixels at 96 DPI = 12" x 8.5"
# Still too big for 10"x7.5" slide
# Use 2x = 768x544 pixels at 96 DPI = 8" x 5.67"
# EMU: width = 7315200, height = 5181600
# Center: x = (10" - 8") / 2 = 1" = 914400 EMU
# Center vertically: y = (7.5" - 5.67") / 2 = 0.92" = 840528 EMU

slide28_path = Path('presentation-unpacked/ppt/slides/slide28.xml')
slide28_rels = Path('presentation-unpacked/ppt/slides/_rels/slide28.xml.rels')

add_image_to_slide(
    slide28_path,
    slide28_rels,
    'rId2',
    '../media/image7.png',
    914400,    # x: 1"
    840528,    # y: 0.92"
    7315200,   # width: 8"
    5181600,   # height: 5.67"
    11,        # pic id
    'Lesson Screenshot'
)

print("\n✓ Images inserted successfully!")
