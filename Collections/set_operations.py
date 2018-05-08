def set_ops():

    blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
    blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
    smell_hcn = {'Harry', 'Amelia'}
    taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
    o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
    b_blood = {'Amelia', 'Jack'}
    a_blood = {'Harry'}
    ab_block = {'Joshua', 'Lola'}

    # find everyone with blues or blond hair
    print(blue_eyes.union(blond_hair))
    print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))

    # Find everyone  with blue eyes and blond hair
    print(blue_eyes.intersection(blond_hair))
    print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))

    # find everyone with blond hair who don't have blue eyes
    print(blond_hair.difference(blue_eyes))
    # non commutative
    print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))

    print(blond_hair.symmetric_difference(blue_eyes))
    print(blond_hair.symmetric_difference(blue_eyes)==blue_eyes.symmetric_difference(blond_hair))

    # Check is one is a subset of another set
    print(smell_hcn.issubset(blond_hair))

    # Check is folks who can smell cyanide can task ptc
    print(taste_ptc.issuperset(smell_hcn))

    # test if sets have no members in common
    print(a_blood.isdisjoint(o_blood))



def main():
    set_ops()


if __name__ == '__main__':
    main()
