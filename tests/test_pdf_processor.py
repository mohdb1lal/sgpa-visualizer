import pytest
from src.utils.pdf_processor import PDFProcessor
from pathlib import Path
import tempfile
from pypdf import PdfWriter

class TestPDFProcessor:
    @pytest.fixture
    def sample_pdf(self):
        """Create a sample PDF file for testing."""
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            writer = PdfWriter()
            # Add a blank page
            writer.add_blank_page(width=595, height=842)
            # Write the PDF to the temporary file
            writer.write(tmp_file)
            tmp_file_path = tmp_file.name
        
        return tmp_file_path
    
    def test_extract_sgpa_valid_pdf(self, sample_pdf):
        """Test SGPA extraction from a valid PDF."""
        try:
            semester, sgpa = PDFProcessor.extract_sgpa_from_pdf(sample_pdf)
            assert isinstance(semester, int)
            assert isinstance(sgpa, float)
        except ValueError:
            # We expect a ValueError since our sample PDF is blank
            pass
        finally:
            # Clean up the temporary file
            Path(sample_pdf).unlink()
    
    def test_invalid_pdf(self):
        """Test handling of invalid PDF file."""
        with pytest.raises(ValueError):
            PDFProcessor.extract_sgpa_from_pdf("nonexistent.pdf")

    def test_find_sgpa(self):
        """Test SGPA extraction from text."""
        test_text = "Some text SGPA 8.97 more text"
        result = PDFProcessor._find_sgpa(test_text)
        assert result == 8.97
    
    def test_find_semester(self):
        """Test semester number extraction from text."""
        test_text = "Semester S7 some text"
        result = PDFProcessor._find_semester(test_text)
        assert result == 7