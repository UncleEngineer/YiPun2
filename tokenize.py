import fugashi
import tinysegmenter
# text = "私はタイ人です。"
text = u'スマートフォンやタブレット端末、インターネット接続テレビ向けストリーミングサービスなどでNHKワールド JAPANを視聴できる無料アプリを提供しています。 スマートフォンやタブレット端末向けのアプリでは、ブレイキングニュース・災害情報を端末に通知するサービスが付いています。'

tagger = fugashi.Tagger()
words = [word.surface for word in tagger(text)]
print(' | '.join(words))

print('-----------')
segmenter = tinysegmenter.TinySegmenter()
print(' | '.join(segmenter.tokenize(text)))