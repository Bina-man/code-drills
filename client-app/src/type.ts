export interface Cell {
    Value: string;
    Attributes?: Array<{ Value: string; Id: string }>;
  }
  
  export interface Row {
    RowType: string;
    Title?: string;
    Cells: Cell[];
    Rows?: Row[];
  }
  
  export interface Report {
    ReportID: string;
    ReportName: string;
    ReportType: string;
    ReportTitles: string[];
    ReportDate: string;
    UpdatedDateUTC: string;
    Fields: any[];  // You can define this type more specifically if you know the structure
    Rows: Row[];
  }