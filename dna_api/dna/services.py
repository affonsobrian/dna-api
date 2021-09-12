from typing import List  # pragma: no cover


class DNAService:  # pragma: no cover
    @staticmethod
    def _dna_iteration_counter(
        i: int,
        j: int,
        data: List[str],
        count: int,
        mutant_count: int,
        last_letter: str,
        search_size: int,
    ) -> tuple:
        if count == search_size:
            mutant_count += 1
            count = 0
            last_letter = None
        if data[i][j] == last_letter or last_letter is None:
            count += 1
        else:
            count = 1
        last_letter = data[i][j]
        return count, mutant_count, last_letter

    @staticmethod
    def is_mutant(data: List[str], search_size: int = 4) -> bool:
        x = len(data)
        y = 0 if x == 0 else len(data[0])

        mutant_count = 0

        for j in range(y):
            count = 0
            last_letter = None
            for i in range(x):
                count, mutant_count, last_letter = DNAService._dna_iteration_counter(
                    i, j, data, count, mutant_count, last_letter, search_size
                )
                if mutant_count > 1:
                    return True

        for i in range(x):
            count = 0
            last_letter = None
            for j in range(y):
                count, mutant_count, last_letter = DNAService._dna_iteration_counter(
                    i, j, data, count, mutant_count, last_letter, search_size
                )
                if mutant_count > 1:
                    return True

        return False
