from core.ui_objects.document import Document
from core.ui_objects.paragraph import Paragraph
from core.ui_objects import Section
from core.writer.recording_tools import create_docx2

xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:tbl>
      <w:tr>
        <w:tc>
          <w:p>
            <w:r>
              <w:t>X</w:t>
            </w:r>
          </w:p>
        </w:tc>
      </w:tr>
    </w:tbl>
  </w:body>
</w:document>"""

create_docx2(xml, "t.docx")
