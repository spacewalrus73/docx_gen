from core.ui_objects.document import Document

from core.ui_objects import CLASS_REGISTRY
print(CLASS_REGISTRY)


from core.oxml_magic.parser import make_xml_tree, to_xml_str

doc = Document("image_word.docx")

tree = make_xml_tree(doc)
print(to_xml_str(tree))


