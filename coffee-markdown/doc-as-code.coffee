fs      = require 'fs'
marked = require 'marked'
markedast  = require 'marked-ast'
markdown = require 'marked-ast-markdown'
coffeescript = require 'coffee-script'
_ = require 'lodash'

Model = (schema) -> (params...) ->
  obj = {}; keys = _.keys schema
  obj[key] = params[i] for i, key of keys
  obj

genTableRow = (keys, header=false) ->
  keys.map (k, i) ->
    val = if _.isArray(k) and k.length
      (k.map (k_) -> k_[(_.keys k_)[0]]).map((i) ->  "<a href=\"##{i}\">#{i}</a>").reduce (prev, cur) -> "#{prev}, #{cur}"
    else
      k
    if not header and i is 0 then val = "<a name=\"#{val}\"></a>#{val}"
    type: 'tablecell', content: ["#{val}"], flags: { header: header, align: null }

table = (collection) ->
  keys = _.keys collection[0]
  type: 'table'
  header: [ type: 'tablerow', content: genTableRow keys, true]
  body: collection.map (item) -> type: 'tablerow', content: genTableRow _.values(item), false

link = (collection, selector) ->
  key = _.keys(selector)[0]
  items = _.filter collection, (item) -> selector[key].call(item)
  (items.map (i) -> i[key]).reduce (prev, curr) -> "#{prev}, #{curr}"

evalWithinContext = (context, code) ->
  ((code) -> eval code ).apply context, [code]

context = {}
renderCode = (code) ->
  output = evalWithinContext context, (coffeescript.compile code, bare:true)
  unless output
    { type: 'paragraph', text: [ '' ] }
  else
    output

contents = fs.readFileSync process.argv[2]
ast = markedast.parse "#{contents}"
ast = ast.map (item) ->
  if item.type is 'code' then renderCode item.code
  else item


markdown = markdown ast
console.log markdown
