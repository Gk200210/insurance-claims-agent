# Autonomous Insurance Claims Processing Agent

## Overview
AI agent that extracts structured data from FNOL insurance documents,
validates required fields, and routes claims using rule-based logic.

## Architecture
PDF → Text Extraction → LLM Field Extraction → Validation → Rule Engine → JSON Output

## Features
✔ Extracts structured fields using OpenAI  
✔ Detects missing mandatory information  
✔ Routes claims automatically  
✔ Provides reasoning for decisions  

## Tech Stack
- Python
- FastAPI
- OpenAI API
- pdfplumber

## Run Instructions
1. Install dependencies: pip install -r requirements.txt
2. Add OPENAI_API_KEY to .env
3. Run: uvicorn app:app --reload
4. Visit /docs and upload sample FNOL document

🧠 Autonomous Insurance Claims Processing Agent

This project implements an AI-powered agent that processes First Notice of Loss (FNOL) insurance documents and automatically routes claims based on predefined rules.

🎯 Objective

Automate extraction, validation, and routing of insurance claims from FNOL documents such as the standardized automobile loss form from ACORD.