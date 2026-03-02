# Resume-optimizer

This project uses the OpenAI Python client. Recent versions (>=1.0.0) removed the `ChatCompletion` API; code has been migrated to the new `client.responses.create` interface.

### Configuration
- **API Key**: set `OPENAI_API_KEY` in your shell before running (`export OPENAI_API_KEY=sk-...`).
- You may also create a `.env` file at the project root with a line like `OPENAI_API_KEY=sk-...`; the application will load it automatically if you install `python-dotenv` (included in `requirements.txt`).
- Streamlit users can alternatively store it in `~/.streamlit/secrets.toml` under `OPENAI_API_KEY`.

Ensure the key is available or the app will raise an error during startup. The helper in `tools/keyword_extractor.py` will provide a clear message if the variable is missing.

- **Model selection**: by default the code uses `gpt-3.5-turbo`, which is accessible to all users. If you have access to other models (e.g. `gpt-4`), set the `OPENAI_MODEL` environment variable to the desired name. Refer to OpenAI’s model list for options.


