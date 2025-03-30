#!/bin/bash
echo "Building LaTeX Research Paper..."
pdflatex research_paper.tex
pdflatex research_paper.tex
echo "Cleaning up temporary files..."
rm -f *.aux *.log *.out *.toc *.lof *.lot
echo "Done! Output file: research_paper.pdf" 