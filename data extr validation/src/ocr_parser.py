import boto3
import os
from typing import Dict, Any
from dotenv import load_dotenv
import re


def extract_from_pdf(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'rb') as file:
        bytes_data = file.read()
        
        response = self.textract.detect_document_text(Document={'Bytes': bytes_data})
      
        raw_text = ' '.join([item['Text'] for item in response['Blocks'] if item['BlockType'] == 'LINE'])
        
        date = self._extract_date(raw_text)
        amount = self._extract_amount(raw_text)
        
        return {
            'raw_text': raw_text,
            'extracted_fields': {
                'date': date,
                'amount': amount
            }
        }

def _extract_date(self, text: str) -> str:
    match = re.search(self.date_pattern, text)
    return match.group() if match else ''

def _extract_amount(self, text: str) -> str:
    match = re.search(self.amount_pattern, text)
    return match.group() if match else ''
