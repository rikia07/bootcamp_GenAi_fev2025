from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Charger la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

print("🔑 Clé API détectée ?" , "✅ Oui" if api_key else "❌ Non")

# Tester l'appel à Gemini
try:
    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-pro-001",
        temperature=0.2,
        GOOGLE_API_KEY=api_key
    )

    print("🧠 Test d'appel à Gemini...")
    response = llm.invoke("Donne-moi une astuce Python simple.")
    print("✅ Réponse de Gemini :\n")
    print(response)

except Exception as e:
    print("❌ Erreur lors de l'appel à Gemini :")
    import traceback
    traceback.print_exc()  # 🔁 Ajoute cette ligne pour afficher les détails