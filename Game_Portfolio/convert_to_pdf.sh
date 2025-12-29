#!/bin/bash
# =============================================================================
# BA Portfolio - Markdown to PDF Converter
# Converts all .md files to PDF with Mermaid diagram support
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BA_PORTFOLIO_DIR="$SCRIPT_DIR"
OUTPUT_DIR="$BA_PORTFOLIO_DIR/PDF_Output"

echo -e "${CYAN}============================================${NC}"
echo -e "${CYAN}   BA Portfolio - MD to PDF Converter      ${NC}"
echo -e "${CYAN}============================================${NC}"
echo ""

# Check if md-to-pdf is installed
check_dependencies() {
    echo -e "${YELLOW}[1/4] Checking dependencies...${NC}"
    
    if ! command -v npm &> /dev/null; then
        echo -e "${RED}[ERROR] npm is not installed. Please install Node.js first.${NC}"
        echo "       Visit: https://nodejs.org/"
        exit 1
    fi
    
    if ! command -v md-to-pdf &> /dev/null; then
        echo -e "${YELLOW}[INFO] Installing md-to-pdf globally...${NC}"
        npm install -g md-to-pdf
    fi
    
    echo -e "${GREEN}[OK] All dependencies are installed.${NC}"
}

# Create output directory
setup_output_dir() {
    echo -e "${YELLOW}[2/4] Setting up output directory...${NC}"
    
    mkdir -p "$OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR/01_Business_Context"
    mkdir -p "$OUTPUT_DIR/02_Requirements_Analysis"
    mkdir -p "$OUTPUT_DIR/03_System_Design"
    mkdir -p "$OUTPUT_DIR/04_Interface_Integration"
    mkdir -p "$OUTPUT_DIR/05_NFR_Metrics"
    mkdir -p "$OUTPUT_DIR/06_SRS"
    
    echo -e "${GREEN}[OK] Output directory created: $OUTPUT_DIR${NC}"
}

# Convert files
convert_files() {
    echo -e "${YELLOW}[3/4] Converting Markdown files to PDF...${NC}"
    echo ""
    
    local count=0
    local total=$(find "$BA_PORTFOLIO_DIR" -name "*.md" -type f | wc -l | tr -d ' ')
    
    # Find all .md files and convert
    while IFS= read -r md_file; do
        # Skip if in PDF_Output directory
        if [[ "$md_file" == *"PDF_Output"* ]]; then
            continue
        fi
        
        ((count++))
        
        # Get relative path
        rel_path="${md_file#$BA_PORTFOLIO_DIR/}"
        
        # Create output path
        pdf_file="$OUTPUT_DIR/${rel_path%.md}.pdf"
        pdf_dir=$(dirname "$pdf_file")
        mkdir -p "$pdf_dir"
        
        echo -e "  [${count}/${total}] Converting: ${CYAN}$rel_path${NC}"
        
        # Convert using md-to-pdf with Mermaid support
        md-to-pdf "$md_file" --dest "$pdf_file" \
            --md-file-encoding utf-8 \
            --pdf-options '{"format": "A4", "margin": {"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"}}' \
            2>/dev/null || {
                echo -e "    ${RED}[WARN] Failed to convert: $rel_path${NC}"
            }
        
        if [[ -f "$pdf_file" ]]; then
            echo -e "    ${GREEN}[OK] Created: ${pdf_file#$BA_PORTFOLIO_DIR/}${NC}"
        fi
        
    done < <(find "$BA_PORTFOLIO_DIR" -name "*.md" -type f | sort)
    
    echo ""
}

# Summary
print_summary() {
    echo -e "${YELLOW}[4/4] Conversion Summary${NC}"
    echo -e "${CYAN}--------------------------------------------${NC}"
    
    local pdf_count=$(find "$OUTPUT_DIR" -name "*.pdf" -type f 2>/dev/null | wc -l | tr -d ' ')
    
    echo -e "  📁 Output Directory: ${GREEN}$OUTPUT_DIR${NC}"
    echo -e "  📄 PDF Files Created: ${GREEN}$pdf_count${NC}"
    echo ""
    
    echo -e "${CYAN}Generated PDFs:${NC}"
    find "$OUTPUT_DIR" -name "*.pdf" -type f | sort | while read -r pdf; do
        echo -e "  ✅ ${pdf#$OUTPUT_DIR/}"
    done
    
    echo ""
    echo -e "${GREEN}============================================${NC}"
    echo -e "${GREEN}   Conversion Complete!                    ${NC}"
    echo -e "${GREEN}============================================${NC}"
}

# Main execution
main() {
    check_dependencies
    setup_output_dir
    convert_files
    print_summary
}

main "$@"
