from typing import List, Dict

class PersonalTask:
    def __init__(self, name: str, date: str, category: str):
        self.name = name
        self.date = date
        self.category = category

class TaskManager:
    def __init__(self):
        self.tasks: List[PersonalTask] = []
    
    def add_task(self, name: str, date: str, category: str):
        """เพิ่มงานใหม่เข้าไปในระบบ"""
        new_task = PersonalTask(name, date, category)
        self.tasks.append(new_task)
        print("เพิ่มงานเรียบร้อยแล้ว")
    
    def show_all_tasks(self):
        """แสดงรายการงานทั้งหมด"""
        if not self.tasks:
            print("ไม่มีงานในระบบ")
            return
        
        print("\nรายการงานทั้งหมด:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.date} - {task.name} ({task.category})")
    
    def delete_task(self, task_index: int):
        """ลบงานออกจากระบบ"""
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"ลบงาน: {removed_task.name} เรียบร้อยแล้ว")
        else:
            print("หมายเลขงานไม่ถูกต้อง")
    
    def summarize_tasks(self):
        """สรุปจำนวนงานตามประเภท"""
        if not self.tasks:
            print("ไม่มีงานในระบบ")
            return
        
        category_counts: Dict[str, int] = {}
        for task in self.tasks:
            category_counts[task.category] = category_counts.get(task.category, 0) + 1
        
        print("\nสรุปจำนวนงานตามประเภท:")
        for category, count in category_counts.items():
            print(f"- {category}: {count} งาน")

def display_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*40)
    print("ระบบจัดการงานส่วนบุคคล")
    print("="*40)
    print("1. เพิ่มงานใหม่")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานตามประเภท")
    print("5. ออกจากโปรแกรม")
    print("="*40)

def main():
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("เลือกเมนู (1-5): ").strip()
        
        if choice == "1":
            name = input("ชื่องาน: ")
            date = input("วันที่ (dd/mm/yyyy): ")
            category = input("ประเภทงาน (งานบ้าน/การเรียน/สุขภาพ/การเงิน/อื่นๆ): ")
            manager.add_task(name, date, category)
        
        elif choice == "2":
            manager.show_all_tasks()
        
        elif choice == "3":
            manager.show_all_tasks()
            if manager.tasks:
                try:
                    task_num = int(input("กรอกหมายเลขงานที่ต้องการลบ: "))
                    manager.delete_task(task_num)
                except ValueError:
                    print("กรุณากรอกตัวเลขเท่านั้น")
        
        elif choice == "4":
            manager.summarize_tasks()
        
        elif choice == "5":
            print("\nขอบคุณที่ใช้ระบบจัดการงานส่วนบุคคล!")
            break
        
        else:
            print("กรุณาเลือกเมนู 1-5 เท่านั้น")

if __name__ == "__main__":
    main()