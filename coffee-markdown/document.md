
# Chapter 1

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi laoreet vel metus at convallis. Integer elit erat, gravida eget rutrum vel, porttitor in odio.
Mauris diam dolor, scelerisque eu **ultricies** sit amet, aliquet sed sapien. Nunc sit amet aliquet sapien, eget sodales erat. Sed finibus leo mauris, ac euismod ex elementum eget.

    @Source = (@id, @title) ->

We have defined the source class. Now we define some sources that are applicable to this project.

    source1 = new @Source 'src1', 'some source2'

    @sources = [
      source1
    ,
      id: 'src2'
      title: 'other title'
    ,
      id: 'src3'
      title: 'my new source'
    ,
      id: 'othersrc'
      title: 'some title2'
    ,
      id: 'somekey'
      title: 'source bla'
    ]

    table @sources

Mauris diam dolor, scelerisque eu **ultricies** sit amet, aliquet sed sapien. Nunc sit amet aliquet sapien, eget sodales erat. Sed finibus leo mauris, ac euismod ex elementum eget.

    customLink = (src, selector) -> "Links: #{link src, selector}"

    @requirements = [
      name: 'req1'

      sources: link @sources, title: -> @id is 'somekey'
    ,
      name: 'req2'
      sources: customLink @sources, title: -> @id in ['src1', 'src2', 'othersrc']
    ]

# Show the requirements

Mauris diam dolor, scelerisque eu **ultricies** sit amet, aliquet sed sapien. Nunc sit amet aliquet sapien, eget sodales erat. Sed finibus leo mauris, ac euismod ex elementum eget.

    table @requirements
