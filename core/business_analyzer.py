class BusinessIdeaAnalyzer:
    def __init__(self, ai_service):
        self.ai_service = ai_service

    def refine_idea(self, vague_idea: str):
        if not vague_idea.strip():
            return "Error: Business idea cannot be empty."
        prompt = f"Please refine the following vague startup idea: '{vague_idea}'"
        return self.ai_service.get_ai_feedback(prompt)
