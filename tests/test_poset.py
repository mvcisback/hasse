from hasse import PoSet


def test_smoke():
    poset = PoSet.from_chains(
        [0b000, 0b001, 0b011, 0b111],
        [0b000, 0b010, 0b011, 0b111],
        [0b000, 0b100, 0b110, 0b111],
        [       0b001, 0b101,      ],
        [       0b010, 0b110,      ],
        [       0b100, 0b101,      ],
    )
    assert len(poset) == 8
    assert set(poset) == set(range(8))
    
    assert poset.compare(0b000, 0b111) == "<"
    assert poset.compare(0b111, 0b000) == ">"
    assert poset.compare(0b001, 0b010) == "||"
    assert poset.compare(0b000, 0b000) == "="

    assert 0b000 in poset
    assert 'x' not in poset

    poset2 = poset.add(['x'])
    assert 'x' not in poset
    assert 'x' in poset2
    assert 0b000 in poset2

    poset3 = poset.add([0b010, 0b001])
    assert poset3.compare(0b010, 0b001) == '<'
