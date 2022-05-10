CREATE TABLE Presidency_Data.tbl_students (
  students_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  students_ldsyv VARCHAR(120)  NULL,
  students_oam6sb4 VARCHAR(120)  NULL,
  students__1mfmyy4hb VARCHAR(120)  NULL,
  students_da13a8dmye8tlsey VARCHAR(120)  NULL,
  students_is_valid BIT NOT NULL DEFAULT 1,
  students_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  students_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  students_deleted_at DATETIME NULL,
  students_creator_id INT NULL,
  students_updater_id INT NULL,
  students_deleter_id INT NULL
)
;

GO
CREATE TABLE Presidency_Data.tbl__8u11ects (
  _8u11ects_id INT NOT NULL PRIMARY KEY IDENTITY(1,1),
  _8u11ects__63t8 VARCHAR(120)  NULL,
  _8u11ects_s5bm6m1d5tv VARCHAR(120)  NULL,
  _8u11ects_wt VARCHAR(120)  NULL,
  _8u11ects_students_sc_id INT  NULL FOREIGN KEY REFERENCES Presidency_Data.tbl_students(students_id),
  _8u11ects_is_valid BIT NOT NULL DEFAULT 1,
  _8u11ects_created_at DATETIME NOT NULL DEFAULT GETDATE(),
  _8u11ects_updated_at DATETIME NOT NULL DEFAULT GETDATE(),
  _8u11ects_deleted_at DATETIME NULL,
  _8u11ects_creator_id INT NULL,
  _8u11ects_updater_id INT NULL,
  _8u11ects_deleter_id INT NULL
)
;

GO
