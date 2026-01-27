#!/usr/bin/env python3

# CountedIterator class
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # الأصلي iterator للكائن
        self.count = 0  # عداد العناصر المسترجعة

    def __next__(self):
        # جلب العنصر التالي وزيادة العداد
        item = next(self.iterator)  # قد يرفع StopIteration تلقائياً عند نهاية العناصر
        self.count += 1
        return item

    def get_count(self):
        # إرجاع عدد العناصر التي تم استرجاعها حتى الآن
        return self.count
