import argparse
import argparseqt.gui

parser = argparse.ArgumentParser(description='Main settings')
parser.add_argument('--storeConst', action='store_const', const=999)

textSettings = parser.add_argument_group('Strings', description='Text input')
textSettings.add_argument('--freetext', type=str, default='Enter freetext here', help='Type anything you want here')
textSettings.add_argument('--pickText', default='I choo-choo-choose you', choices=['Bee mine', 'I choo-choo-choose you'], help='Choose one of these')

app = QtWidgets.QApplication()
dialog = argparseqt.gui.ArgDialog(parser)
dialog.exec_()

if dialog.result() == QtWidgets.QDialog.Accepted:
	values = dialog.getValues()
	print('Values:', values)
else:
	print('User cancelled')