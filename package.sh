#!/bin/bash
echo "Packaging AI Calculator for submission..."
zip -r AI_Calculator_Submission.zip . -x "*.git*" "*.env" "*.venv*" "__pycache__/*" "*.pytest_cache*" "*.DS_Store*"
echo "Complete! Saved to AI_Calculator_Submission.zip"
