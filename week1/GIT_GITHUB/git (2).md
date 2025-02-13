1. Creer un dossier
2. Je veux que mon dossier soit gerer par git
3. Je rentre dans mon dossier sur le terminal

git init 

On fait cette etape une fois par dossier

4. J'ai travaillé/codé ..
5. Je veux sauvegarder mon travail

6. Je rentre dans mon terminal (faire attention de  bien être dans le chemin du dossier)

git add .

cette étape permet de rassembler toutes les modifications

7. Je veux sauvegarder mon travail

git commit -m "mon commentaire pour m'aider à gerer mes versions"

8. 
git branch -M main

A faire uniquement une fois

9. Creer un token classique

A faire uniquement une fois

10. Pour lier ,on dossier local a mon github repository

git remote add origin https://[TOKEN]@github.com/[REPO-OWNER]/[REPO-NAME]

A faire uniquement une fois

10. Pour pusher le contenu sur le github
git push -u origin main
