from room import app
from helpers import xml_node_name
@app.route("/url3/pay/list/category/03.xml")
@xml_node_name("PayCategoryList")
def pay_list_category_list():
    # TODO: revert from temporary, pre-determined value to database schema
    filler = []
    for i in range(64):
        # Items must be indexed by 1.
        filler.append(
            RepeatedElement(
                {
                    "place": i + 1,
                    "categid":12345,
                    "name": "Testing...",
                    "sppageid": 0,
                    "splinktext": "Link Text"
                }
            )
        )

    return {
        "type":3,
        "img": 0,
        "categinfo": filler,
    }
