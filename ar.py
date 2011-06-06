# -*- coding: utf-8 -*-

from transactions import TransactionsList
from args import process_args
from apriori import Apriori
from dic import Dic
from stats import Stats
from rules import RulesGenerator
from writer import Writer

def main(args):
    stats = Stats()
    transactions = TransactionsList(args.infile)
    if args.algorithm == 'apriori':
        apriori = Apriori(transactions, args.minsup)
        large_sets, counter = apriori.get_large_sets_and_counter()
    else:
        dic = Dic(transactions, args.minsup, args.m)
        large_sets = dic.get_large_sets()
    stats.record_post_large_sets()
    rules = RulesGenerator.generate_rules(large_sets, args.minconf, counter, transactions)
    stats.record_post_rules()

    writer = Writer(args.outfile)
    writer.add_args(args)
    writer.add_stats(stats)
    writer.add_rules(rules)
    writer.write()

if __name__ == '__main__':
    args = process_args()
    main(args)
