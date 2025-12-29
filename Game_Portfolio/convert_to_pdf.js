const { mdToPdf } = require('md-to-pdf');
const fs = require('fs');
const path = require('path');

// Configuration
const BA_PORTFOLIO_DIR = __dirname;
const OUTPUT_DIR = path.join(BA_PORTFOLIO_DIR, 'PDF_Output');

// PDF Options
const pdfOptions = {
    pdf_options: {
        format: 'A4',
        margin: {
            top: '20mm',
            bottom: '20mm',
            left: '15mm',
            right: '15mm'
        },
        printBackground: true
    },
    stylesheet: [],
    css: `
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
        }
        h1 { color: #2196F3; border-bottom: 2px solid #2196F3; padding-bottom: 10px; }
        h2 { color: #1976D2; margin-top: 30px; }
        h3 { color: #1565C0; }
        table { border-collapse: collapse; width: 100%; margin: 15px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f5f5f5; font-weight: bold; }
        tr:nth-child(even) { background-color: #fafafa; }
        code { background-color: #f5f5f5; padding: 2px 6px; border-radius: 3px; }
        pre { background-color: #f5f5f5; padding: 15px; border-radius: 5px; overflow-x: auto; }
        blockquote { border-left: 4px solid #2196F3; padding-left: 15px; margin-left: 0; color: #666; }
    `,
    launch_options: {
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }
};

// Find all .md files recursively
function findMarkdownFiles(dir, files = []) {
    const items = fs.readdirSync(dir);
    
    for (const item of items) {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        
        if (stat.isDirectory()) {
            // Skip output directory and node_modules
            if (item !== 'PDF_Output' && item !== 'node_modules') {
                findMarkdownFiles(fullPath, files);
            }
        } else if (item.endsWith('.md')) {
            files.push(fullPath);
        }
    }
    
    return files;
}

// Create output directory structure
function createOutputDirs() {
    const dirs = [
        OUTPUT_DIR,
        path.join(OUTPUT_DIR, '01_Business_Context'),
        path.join(OUTPUT_DIR, '02_Requirements_Analysis'),
        path.join(OUTPUT_DIR, '03_System_Design'),
        path.join(OUTPUT_DIR, '04_Interface_Integration'),
        path.join(OUTPUT_DIR, '05_NFR_Metrics'),
        path.join(OUTPUT_DIR, '06_SRS')
    ];
    
    for (const dir of dirs) {
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }
    }
}

// Convert a single file
async function convertFile(mdPath) {
    const relativePath = path.relative(BA_PORTFOLIO_DIR, mdPath);
    const pdfPath = path.join(OUTPUT_DIR, relativePath.replace('.md', '.pdf'));
    const pdfDir = path.dirname(pdfPath);
    
    // Ensure output directory exists
    if (!fs.existsSync(pdfDir)) {
        fs.mkdirSync(pdfDir, { recursive: true });
    }
    
    try {
        const pdf = await mdToPdf(
            { path: mdPath },
            pdfOptions
        );
        
        if (pdf) {
            fs.writeFileSync(pdfPath, pdf.content);
            console.log(`  ✅ ${relativePath} → ${path.relative(BA_PORTFOLIO_DIR, pdfPath)}`);
            return true;
        }
    } catch (error) {
        console.log(`  ❌ ${relativePath}: ${error.message}`);
        return false;
    }
    
    return false;
}

// Main function
async function main() {
    console.log('============================================');
    console.log('   BA Portfolio - MD to PDF Converter');
    console.log('============================================\n');
    
    console.log('[1/3] Setting up output directory...');
    createOutputDirs();
    console.log(`      Output: ${OUTPUT_DIR}\n`);
    
    console.log('[2/3] Finding Markdown files...');
    const files = findMarkdownFiles(BA_PORTFOLIO_DIR);
    console.log(`      Found ${files.length} files\n`);
    
    console.log('[3/3] Converting files...\n');
    
    let successCount = 0;
    for (const file of files.sort()) {
        const success = await convertFile(file);
        if (success) successCount++;
    }
    
    console.log('\n============================================');
    console.log(`   Conversion Complete!`);
    console.log(`   Successfully converted: ${successCount}/${files.length} files`);
    console.log('============================================');
}

main().catch(console.error);
