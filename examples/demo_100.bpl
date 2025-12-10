< Beacon 100% - Final Working Demo >

blueprint Box {
    shard value
}

firm b = spawn Box()
b.value = 42
show("Property test:")
show(b.value)

show("Beacon 100% Complete!")
