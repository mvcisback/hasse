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
    assert poset.add(['x'])
    assert 'x' in poset
    assert 0b000 in poset
