fs      = require 'fs'
marked = require 'marked'
markedast  = require 'marked-ast'
markdown = require 'marked-ast-markdown'
coffeescript = require 'coffee-script'
_ = require 'lodash'

Model = (schema) -> (params...) ->
  keys = _.keys schema
  obj = {}
  obj[key] = params[i] for i, key of keys
  obj


genTableRow = (keys, header=false) ->
  keys.map (k) ->
    val = if _.isArray k
      k.map (k_) -> ",#{k_[(_.keys k_)[0]]}"
    else
      [k]
    type: 'tablecell', content: val, flags: { header: header, align: null }

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
    # console.log 'output', output
    # console.log 'code', coffeescript.compile code, bare:true
    # console.log code
    # "error generating code"
    { type: 'paragraph', text: [ '' ] }
  else
    output

filepath =  process.argv[2]
contents = fs.readFileSync filepath

ast = markedast.parse "#{contents}"

ast = ast.map (item) ->
  if item.type is 'code'
    renderCode item.code
  else
    item

# console.log ast

console.log markdown ast


#type: 'code',
# code: '@sources = [\n  id: \'src1\'\n  title: \'some title\'\n,\n  id: \'src2\'\n  title: \'other title\'\n]\n\ntable @sources',

# { type: 'table',
#   header: [ { type: 'tablerow', content: [Object] } ],
#   body: [ { type: 'tablerow', content: [Object] } ] }

# { type: 'tablerow', content: [ [Object], [Object], [Object] ]

#[ { type: 'tablecell',
  #   content: [ 'a' ],
  #   flags: { header: true, align: null } },
  # { type: 'tablecell',
  #   content: [ 'b' ],
  #   flags: { header: true, align: null } },
  # { type: 'tablecell',
  #   content: [ 'c' ],
  #   flags: { header: true, align: null } } ]
