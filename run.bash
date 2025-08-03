docker run \
  -e FLASK_ENV=production \
  -e OPENAI_API_KEY=sk-123 \
  -e DATABASE_URL="postgresql://user:pass@host:port/db" \
  my-image
