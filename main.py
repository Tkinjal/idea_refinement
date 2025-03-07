from config.config import API_KEY
from services.ai_service import AIService
from core.business_analyzer import BusinessIdeaAnalyzer


def main():
    ai_service = AIService(API_KEY)
    analyzer = BusinessIdeaAnalyzer(ai_service)

    vague_idea = input("Please enter a vague startup idea: ").strip()
    refined_idea = analyzer.refine_idea(vague_idea)

    print("\nVague Idea:", vague_idea)
    print("Refined Idea:", refined_idea)


if __name__ == "__main__":
    main()
