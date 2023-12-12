from visidata import vd, TableSheet, ExprColumn

phone_pad = {
    "abc": 2,
    "def": 3,
    "ghi": 4,
    "jkl": 5,
    "mno": 6,
    "pqrs": 7,
    "tuv": 8,
    "wxyz": 9,
}

vd.phone_lookup = str.maketrans(
    {letter: str(number) for letters, number in phone_pad.items() for letter in letters}
)


@TableSheet.api
def phoneKeysFor(sheet, col):
    newcol = ExprColumn("curcol.lower().replace(' ','').translate(vd.phone_lookup)", curcol=col)
    newcol.name = f"{col.name}_phonekeys"
    sheet.addColumnAtCursor(newcol)


TableSheet.addCommand("", "phone-keys-for-col", "sheet.phoneKeysFor(cursorCol)")
