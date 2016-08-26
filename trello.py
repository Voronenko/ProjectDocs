#!/usr/bin/python
import trolly
import os

def linesWithPadding(text, padding):
  paddingstring = " " * padding
  result = []
  rows = text.split('\n')
  for row in rows:
    result.append((paddingstring + row).encode('UTF-8'))
  return result

client = trolly.client.Client(os.environ['trello_api_key'], os.environ['trello_token')

print('Member: %s' % client.get_member())

# print('Organisations:')
# for organisation in client.get_organisations():
#     print(' - %s' % organisation)
#
# print('Organisations:')
# for organisation in client.get_organisations():
#     print(' - %s' % organisation)

# print('Boards:')
# boards = client.get_boards()
# for board in boards:
#     print(' - %s' % board)

# decodeon u'5771804b1f066800d990983f'


board = client.get_board('5771804b1f066800d990983f')

lists = board.get_lists()

print('Cards:')
cards = board.get_cards(board_id='5771804b1f066800d990983f')
# for card in cards:
#     print(' - %s' % card)

# Get all information from a card (works for boards, lists, etc. too):
# print('Detailed cards:')
# for card in client.get_cards(actions='all'):
#     print(' - %s: %s' % (card, card.data))



# Open a file in write mode
fo = open("docs/trello.rst", "w")
fo.write('====================\r\n')
fo.write('Trello project board\r\n')
fo.write('====================\r\n')


for list in lists:
  fo.write(list.name)
  fo.write('\r\n')
  fo.write('#' * len(list.name))
  fo.write('\r\n')

  for card in [x for x in cards if x.idList == list.id]:
    fo.write('.. _trl_%s:\r\n' % card.id)
    fo.write('\r\n')
    fo.write('  .. container:: toggle\r\n')
    fo.write('\r\n')
    fo.write('      .. container:: header\r\n')
    fo.write('\r\n')
    fo.write('          **%s**\r\n' % card.name)
    fo.write('          `<%s/>`_\r\n' % card.url)
    fo.write('      .. code-block:: none')
    desclines = linesWithPadding(card.desc, 8)
    fo.write('\r\n')
    fo.write('\r\n')
    for line in desclines:
      fo.write(line)
      fo.write('\r\n')
    fo.write('\r\n')
fo.close()
