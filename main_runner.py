from core.ui_objects.document import Document
from core.ui_objects.paragraph import Paragraph
from core.ui_objects import Section

# s = Section()
# s.change_page_size(width=12240, height=15840)
# print(s.property)
doc = Document("image_word.docx")

bo = doc.objects[0].objects[0].objects[0].objects[1].objects

print(bo)
from core.ui_objects import CLASS_REGISTRY

# print(CLASS_REGISTRY)
# print(bo)
