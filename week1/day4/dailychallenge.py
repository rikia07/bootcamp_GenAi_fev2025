class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)  # Convertir en entier si c'est un float
        self.totalPages = max(1, -(-len(self.items) // self.pageSize))  # Calcul du nombre total de pages
        self.currentPage = 1  # Commence à la première page

    def getVisibleItems(self):
        # Retourne les éléments de la page actuelle.
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def nextPage(self):
        # "Passe à la page suivante si possible.
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self  # Permet le chaînage

    def prevPage(self):
        Passe à la page précédente si possible.
        if self.currentPage > 1:
            self.currentPage -= 1
        return self  # Permet le chaînage

    def firstPage(self):
        """Va à la première page."""
        self.currentPage = 1
        return self  # Permet le chaînage

    def lastPage(self):
        """Va à la dernière page."""
        self.currentPage = self.totalPages
        return self  # Permet le chaînage

    def goToPage(self, pageNum):
        """Va à une page spécifique en respectant les bornes."""
        pageNum = int(pageNum)  # Convertir en entier si c'est un float
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self  

