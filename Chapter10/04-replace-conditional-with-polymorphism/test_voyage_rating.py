from voyage_rating import HistoryObject, VoyageObject, rating


def test_rating():
    voyage = VoyageObject("West India", 10)
    history = [
        HistoryObject("East India", 5),
        HistoryObject("West India", 15),
        HistoryObject("China", -2),
        HistoryObject("West Africa", 7),
    ]
    assert rating(voyage, history) == "B"
