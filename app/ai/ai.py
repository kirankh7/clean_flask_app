import os
from flask import Blueprint, request, jsonify

ai = Blueprint('ai', __name__)


@ai.route('/ask', methods=['POST'])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get('question', '').strip()
    if not question:
        return jsonify(error='question field required'), 400
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        return jsonify(error='AI not configured', hint='Set ANTHROPIC_API_KEY'), 503
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        msg = client.messages.create(
            model='claude-sonnet-4-6',
            max_tokens=1024,
            messages=[{'role': 'user', 'content': question}],
        )
        return jsonify(answer=msg.content[0].text)
    except Exception as e:
        return jsonify(error='AI request failed', detail=str(e)), 500
